from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.forms import CustomSignupForm

User = get_user_model()


class CustomFormsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def init_form_helper(self, form):
        form.helper = FormHelper()
        form.helper.add_input(Submit("submit", "Submit"))

    def test_custom_signup_form(self):
        form_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "password1": "passwordSE123",
            "password2": "passwordSE123",
            "years_of_experience": 5,
        }
        request = self.factory.post(reverse("accounts:account-signup"), data=form_data)
        request.session = {}
        form = CustomSignupForm(data=form_data)
        self.init_form_helper(form)
        self.assertTrue(form.is_valid())
        user = form.save(request)
        self.assertIsInstance(user, User)
