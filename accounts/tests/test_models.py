from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from accounts.models import Redactor


class RedactorModelTest(TestCase):

    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
            first_name="john",
            last_name="doe",
            years_of_experience=5,
            email_verified=True,
        )

    def test_redactor_creation(self):
        self.assertEqual(self.redactor.username, "testuser")
        self.assertEqual(self.redactor.email, "testuser@example.com")
        self.assertTrue(self.redactor.check_password("testpassword123"))
        self.assertEqual(self.redactor.first_name, "John")  # capitalized
        self.assertEqual(self.redactor.last_name, "Doe")  # capitalized
        self.assertEqual(self.redactor.years_of_experience, 5)
        self.assertTrue(self.redactor.email_verified)

    def test_username_validation(self):
        self.redactor.username = "invalid username"
        with self.assertRaises(ValidationError):
            self.redactor.full_clean()

    def test_first_name_validation(self):
        self.redactor.first_name = "invalid123"
        with self.assertRaises(ValidationError):
            self.redactor.full_clean()

    def test_last_name_validation(self):
        self.redactor.last_name = "invalid123"
        with self.assertRaises(ValidationError):
            self.redactor.full_clean()

    def test_get_absolute_url(self):
        expected_url = reverse("board:redactor-detail", kwargs={"pk": self.redactor.pk})
        self.assertEqual(self.redactor.get_absolute_url(), expected_url)

    def test_str_method(self):
        self.assertEqual(str(self.redactor), self.redactor.username)

    def test_required_fields(self):
        required_fields = self.redactor.REQUIRED_FIELDS
        self.assertEqual(set(required_fields), {"username", "first_name", "last_name"})

    def test_username_field_unique(self):
        with self.assertRaises(Exception):
            Redactor.objects.create_user(
                username="testuser",
                email="anotheremail@example.com",
                password="anotherpassword",
            )

    def test_email_field_unique(self):
        with self.assertRaises(Exception):
            Redactor.objects.create_user(
                username="anotheruser",
                email="testuser@example.com",
                password="anotherpassword",
            )
