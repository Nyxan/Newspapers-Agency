from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Redactor, Newspaper


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ('first_name', 'last_name', 'username', 'email', 'years_of_experience', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})
        self.fields['years_of_experience'].widget.attrs.update({'placeholder': 'Years of Experience', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'class': 'form-control'})

class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ('first_name', 'last_name', 'username', 'years_of_experience')


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'topic']