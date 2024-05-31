from django.contrib import admin
from django.test import TestCase
from accounts.models import Redactor
from board.models import Newspaper, Topic
from board.admin import RedactorAdmin, NewspaperAdmin, TopicAdmin


class AdminTestCase(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(
            username="test_user", years_of_experience=5
        )
        self.newspaper = Newspaper.objects.create(title="Test Newspaper")
        self.topic = Topic.objects.create(name="Test Topic")

    def test_redactor_admin(self):
        redactor_admin = RedactorAdmin(Redactor, admin.site)
        self.assertIn("years_of_experience", redactor_admin.list_display)
        self.assertEqual(len(redactor_admin.fieldsets), 5)
        self.assertEqual(len(redactor_admin.add_fieldsets), 2)

    def test_newspaper_admin(self):
        newspaper_admin = NewspaperAdmin(Newspaper, admin.site)
        self.assertIn("title", newspaper_admin.list_display)
        self.assertIn("topic__name", newspaper_admin.list_filter)
        self.assertIn("title", newspaper_admin.search_fields)

    def test_topic_admin(self):
        topic_admin = TopicAdmin(Topic, admin.site)
        self.assertIn("name", topic_admin.list_display)


class AdminSiteTestCase(TestCase):
    def test_admin_sites(self):
        self.assertIn(Redactor, admin.site._registry)
        self.assertIn(Newspaper, admin.site._registry)
        self.assertIn(Topic, admin.site._registry)
