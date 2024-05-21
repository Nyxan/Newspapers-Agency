from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publisher_date = models.DateField(auto_now_add=True)
    topic = models.ManyToManyField(
        Topic, related_name="newspapers"
    )
    redactor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")
    image = models.ImageField(upload_to="newspapers", blank=True, null=True)


    def __str__(self):
        return f"{self.title} {self.publisher_date}"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE, related_name="comments")
    redactor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.redactor.username} on {self.newspaper.title}"
