from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Redactor
from board.models import Newspaper, Topic


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                        "email"
                    )
                },
            ),
        )
    )


class NewspaperAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "publisher_date",
    )
    fields = ("title", "content", "publisher_date", "topic", "redactor", "image")
    filter_horizontal = ("topic", "redactor")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
