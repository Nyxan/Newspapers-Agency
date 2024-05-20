from allauth.account.views import (
    LoginView,
    SignupView,
    PasswordResetView,
    PasswordChangeView,
)
from accounts.forms import *


class CustomLoginView(LoginView):
    form_class = CustomLoginForm


class CustomSignupView(SignupView):
    form_class = CustomSignupForm


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomResetPasswordForm


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomChangePasswordForm
