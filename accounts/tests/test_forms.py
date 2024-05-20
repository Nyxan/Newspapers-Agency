from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import CustomSignupForm, CustomLoginForm, CustomResetPasswordForm, CustomChangePasswordForm, CustomSetPasswordForm

User = get_user_model()

class CustomSignupFormTest(TestCase):
    def test_signup_form_valid(self):
        form_data = {
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 5
        }
        form = CustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save(self.request)
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.redactor.years_of_experience, 5)

    def test_signup_form_invalid(self):
        form_data = {
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password1234',  # Passwords do not match
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 5
        }
        form = CustomSignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

class CustomLoginFormTest(TestCase):
    def test_login_form_valid(self):
        user = User.objects.create_user(email='test@example.com', password='password123')
        form_data = {
            'login': 'test@example.com',
            'password': 'password123'
        }
        form = CustomLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form_data = {
            'login': 'test@example.com',
            'password': 'wrongpassword'
        }
        form = CustomLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomResetPasswordFormTest(TestCase):
    def test_reset_password_form_valid(self):
        user = User.objects.create_user(email='test@example.com', password='password123')
        form_data = {
            'email': 'test@example.com'
        }
        form = CustomResetPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_reset_password_form_invalid(self):
        form_data = {
            'email': 'invalid@example.com'
        }
        form = CustomResetPasswordForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomChangePasswordFormTest(TestCase):
    def test_change_password_form_valid(self):
        user = User.objects.create_user(email='test@example.com', password='password123')
        form_data = {
            'oldpassword': 'password123',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        form = CustomChangePasswordForm(user=user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_change_password_form_invalid(self):
        user = User.objects.create_user(email='test@example.com', password='password123')
        form_data = {
            'oldpassword': 'wrongpassword',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        form = CustomChangePasswordForm(user=user, data=form_data)
        self.assertFalse(form.is_valid())

class CustomSetPasswordFormTest(TestCase):
    def test_set_password_form_valid(self):
        user = User.objects.create_user(email='test@example.com', password='password123')
        form_data = {
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        form = CustomSetPasswordForm(user=user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_set_password_form_invalid(self):
        user = User.objects.create_user(email='test@example.com', password='password123')
        form_data = {
            'password1': 'newpassword123',
            'password2': 'differentpassword123'
        }
        form = CustomSetPasswordForm(user=user, data=form_data)
        self.assertFalse(form.is_valid())