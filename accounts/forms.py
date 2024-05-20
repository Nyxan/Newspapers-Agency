from allauth.account.forms import ChangePasswordForm, ResetPasswordForm, LoginForm, SignupForm, SetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class CustomSignupForm(SignupForm):
    username = forms.CharField(min_length=3, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    years_of_experience = forms.IntegerField()

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.years_of_experience = self.cleaned_data['years_of_experience']
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.helper = FormHelper()
        self.helper.add_input(Submit('signup', 'Sign Up'))


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('login', 'Login'))


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('reset_password', 'Reset Password'))


class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('change_password', 'Change Password'))
