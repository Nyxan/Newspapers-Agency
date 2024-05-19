from django.urls import path
from accounts.views import CustomSignupView, CustomLoginView, CustomPasswordResetView, CustomPasswordChangeView

urlpatterns = [
    path('accountss/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accountss/login/', CustomLoginView.as_view(), name='account_login'),
    path('accountss/password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('accountss/password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
]

app_name = 'accountss'
