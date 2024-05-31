from django.urls import path
from accounts.views import (
    CustomSignupView,
    CustomLoginView,
    CustomPasswordResetView,
    CustomPasswordChangeView,
)

urlpatterns = [
    path("accounts/signup/", CustomSignupView.as_view(), name="account-signup"),
    path("accounts/login/", CustomLoginView.as_view(), name="account-login"),
    path(
        "accounts/password/reset/",
        CustomPasswordResetView.as_view(),
        name="account-reset-password",
    ),
    path(
        "accounts/password/change/",
        CustomPasswordChangeView.as_view(),
        name="account-change-password",
    ),
]

app_name = "accounts"
