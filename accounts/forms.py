from allauth.account.forms import ChangePasswordForm, ResetPasswordForm, LoginForm, SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    years_of_experience = forms.IntegerField(label='Years of Experience')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.years_of_experience = self.cleaned_data['years_of_experience']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    pass


class CustomResetPasswordForm(ResetPasswordForm):
    pass


class CustomChangePasswordForm(ChangePasswordForm):
    pass
