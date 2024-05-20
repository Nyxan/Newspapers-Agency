from django.urls import path
from accounts.views import CustomSignupView, CustomLoginView, CustomPasswordResetView, CustomPasswordChangeView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
]

app_name = 'accounts'
