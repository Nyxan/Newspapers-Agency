from django.test import TestCase
from board.forms import (
    RedactorCreationForm,
    RedactorUpdateForm,
    NewspaperSearchForm,
)
from accounts.models import Redactor


class FormsTestCase(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "years_of_experience": 5,
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_redactor_update_form(self):
        redactor = Redactor.objects.create(
            username="test_user",
            years_of_experience=5)
        form_data = {
            "first_name": "Updated",
            "last_name": "User",
            "email": "updated@example.com",
            "username": "test_user",
            "years_of_experience": 10,
        }
        form = RedactorUpdateForm(data=form_data, instance=redactor)
        self.assertTrue(form.is_valid())

    def test_newspaper_search_form(self):
        form_data = {"title": "Test Title"}
        form = NewspaperSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
