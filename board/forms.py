from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Redactor
from board.models import Newspaper, Topic


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            'email',
            "first_name",
            "last_name",
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ('first_name', 'last_name','email', 'username', 'years_of_experience')


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'topic', 'redactor']
        widgets = {
            'topic': forms.CheckboxSelectMultiple(),
            'redactor': forms.CheckboxSelectMultiple()
        }


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
