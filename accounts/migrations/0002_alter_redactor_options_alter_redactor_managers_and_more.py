# Generated by Django 5.0.6 on 2024-05-18 12:29

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accountss", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="redactor",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterModelManagers(
            name="redactor",
            managers=[],
        ),
        migrations.AlterField(
            model_name="redactor",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="redactor",
            name="first_name",
            field=models.CharField(
                max_length=50, validators=[accounts.validators.validate_name]
            ),
        ),
        migrations.AlterField(
            model_name="redactor",
            name="last_name",
            field=models.CharField(
                max_length=50, validators=[accounts.validators.validate_name]
            ),
        ),
        migrations.AlterField(
            model_name="redactor",
            name="username",
            field=models.CharField(
                max_length=30,
                unique=True,
                validators=[accounts.validators.validate_username],
            ),
        ),
    ]
