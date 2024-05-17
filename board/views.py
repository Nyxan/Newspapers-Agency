from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegistrationForm, RedactorUpdateForm, NewspaperForm
from .models import Redactor, Topic, Newspaper


@login_required
def index(request):

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "board/index.html", context=context)


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "board/redactor_list.html"
    context_object_name = "redactors"
    paginate_by = 5


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers__topic")


@login_required
def create_newspaper(request):
    if request.method == 'POST':
        form = NewspaperForm(request.POST)
        if form.is_valid():
            newspaper = form.save(commit=False)
            newspaper.save()
            newspaper.redactor.add(request.user)
            return redirect('board:newspaper-list')
    else:
        form = NewspaperForm()
    return render(request, 'board/create_newspaper.html', {'form': form})


class RedactorUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("board:redactor-list")
    template_name = "board/redactor_update.html"

    def get_queryset(self):
        """ Limit deletion to the logged-in user """
        qs = super().get_queryset()
        return qs.filter(pk=self.request.user.pk)


class RedactorDelete(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "board/topic_list.html"
    context_object_name = "topics"
    paginate_by = 5


class NewspapersListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "board/newspaper_list.html"
    context_object_name = "newspapers"
    paginate_by = 5


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    context_object_name = "newspaper"


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})
