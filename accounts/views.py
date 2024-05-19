from allauth.account.views import LoginView, SignupView, PasswordResetView, PasswordChangeView
from accounts.forms import RedactorSignupForm, RedactorLoginForm, RedactorResetPasswordForm, RedactorChangePasswordForm


class CustomLoginView(LoginView):
    form_class = RedactorLoginForm
    template_name = 'account/login.html'


class CustomSignupView(SignupView):
    form_class = RedactorSignupForm
    template_name = 'account/signup.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = RedactorResetPasswordForm


class CustomPasswordChangeView(PasswordChangeView):
    form_class = RedactorChangePasswordForm
