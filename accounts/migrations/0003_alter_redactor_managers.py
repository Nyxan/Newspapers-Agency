# Generated by Django 5.0.6 on 2024-05-18 19:03

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_redactor_options_alter_redactor_managers_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="redactor",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
