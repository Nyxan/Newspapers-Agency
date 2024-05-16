from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


class Topic(models.Model):
    name = models.CharField(max_length=100)


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publisher_date = models.DateField(null=True, auto_now_add=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="newspapers"
    )
    author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")
