from allauth.account.forms import ChangePasswordForm, ResetPasswordForm, LoginForm, SignupForm
from django import forms


class RedactorSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    years_of_experience = forms.IntegerField()

    def save(self, request):
        # Save the user and profile
        user = super(RedactorSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.redactor.years_of_experience = self.cleaned_data['years_of_experience']
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RedactorSignupForm, self).__init__(*args, **kwargs)
        # Add fields to the form
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class RedactorLoginForm(LoginForm):
    pass


class RedactorResetPasswordForm(ResetPasswordForm):
    pass


class RedactorChangePasswordForm(ChangePasswordForm):
    pass
