from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from board.forms import RedactorUpdateForm, NewspaperForm, RedactorSearchForm, TopicSearchForm, NewspaperSearchForm, \
    TopicCreateForm, RedactorCreationForm
from board.models import Topic, Newspaper, Comment
from accounts.models import Redactor


@login_required
def index(request):
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    topics = Topic.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_newspapers': num_newspapers,
        'num_redactors': num_redactors,
        'num_topics': num_topics,
        'num_visits': num_visits,
        'topics': topics,
    }

    return render(request, 'board/index.html', context)


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "board/redactor_list.html"
    context_object_name = "redactors"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        context["search_form"] = RedactorSearchForm()
        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'board/redactor_detail.html'
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers__topic")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        redactor = self.get_object()
        newspapers = redactor.newspapers.all()
        paginator = Paginator(newspapers, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            newspapers = paginator.page(page)
        except PageNotAnInteger:
            newspapers = paginator.page(1)
        except EmptyPage:
            newspapers = paginator.page(paginator.num_pages)
        context['newspapers'] = newspapers
        return context


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    template_name = 'board/redactor_form.html'


class RedactorUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("board:redactor-list")
    template_name = "board/redactor_update.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(pk=self.request.user.pk)


class RedactorDelete(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("board:redactor-list")
    template_name = 'board/redactor_confirm_delete.html'


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "board/topic_list.html"
    context_object_name = "topics"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm()
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = 'board/topic_detail.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newspapers'] = self.object.newspapers.all()
        return context


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicCreateForm
    template_name = 'board/topic_form.html'
    success_url = reverse_lazy("board:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("board:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy('board:topic-list')


class NewspapersListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "board/newspaper_list.html"
    context_object_name = "newspapers"
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspapersListView, self).get_context_data(**kwargs)
        context["search_form"] = NewspaperSearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        model = self.request.GET.get("model")
        if model:
            queryset = queryset.filter(model__icontains=model)
        return queryset


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = 'board/newspaper_form.html'
    success_url = reverse_lazy('board:newspaper-list')


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    context_object_name = "newspaper"


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("board:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("board:newspaper-list")


@login_required
def add_comment(request, newspaper_id):
    if request.method == 'POST':
        newspaper = Newspaper.objects.get(id=newspaper_id)
        content = request.POST.get('content')
        redactor = request.user
        Comment.objects.create(newspaper=newspaper, content=content, redactor=redactor)
        return redirect('board:newspaper-detail', pk=newspaper_id)
    else:
        return redirect('board:index')


def newspaper_search(request):
    query = request.GET.get('q', '')
    if query:
        terms = query.split(',')
        include_topics = []
        exclude_topics = []
        include_redactors = []
        exclude_redactors = []

        for term in terms:
            term = term.strip()
            if term.startswith('-'):
                if ' ' in term:
                    exclude_redactors.append(term[1:])
                else:
                    exclude_topics.append(term[1:])
            else:
                if ' ' in term:
                    include_redactors.append(term)
                else:
                    include_topics.append(term)

        include_topic_queries = Q()
        for topic in include_topics:
            include_topic_queries |= Q(topic__name__icontains=topic)

        exclude_topic_queries = Q()
        for topic in exclude_topics:
            exclude_topic_queries |= Q(topic__name__icontains=topic)

        include_redactor_queries = Q()
        for redactor in include_redactors:
            include_redactor_queries |= Q(redactor__username__icontains=redactor)

        exclude_redactor_queries = Q()
        for redactor in exclude_redactors:
            exclude_redactor_queries |= Q(redactor__username__icontains=redactor)

        newspapers = Newspaper.objects.filter(include_topic_queries, include_redactor_queries).exclude(
            exclude_topic_queries).exclude(exclude_redactor_queries).distinct()

        if include_redactors:
            newspapers = newspapers.filter(redactor__username__in=include_redactors).distinct()
        if exclude_redactors:
            newspapers = newspapers.exclude(redactor__username__in=exclude_redactors).distinct()
    else:
        newspapers = Newspaper.objects.none()

    return render(request, 'board/newspaper_search.html', {'newspapers': newspapers, 'query': query})
