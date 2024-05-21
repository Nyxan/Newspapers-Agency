# Generated by Django 5.0.6 on 2024-05-18 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_remove_newspaper_topic_newspaper_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="newspaper",
            name="main_topic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="main_newspapers",
                to="board.topic",
            ),
        ),
    ]
