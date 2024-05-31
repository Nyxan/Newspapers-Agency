from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from accounts.validators import validate_name, validate_username


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    email_verified = models.BooleanField(default=False)
    username = models.CharField(
        max_length=30, unique=True, validators=[validate_username]
    )
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30, validators=[validate_name])
    last_name = models.CharField(max_length=30, validators=[validate_name])
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def get_absolute_url(self):
        return reverse("board:redactor-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)
