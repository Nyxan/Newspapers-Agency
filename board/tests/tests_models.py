from django.test import TestCase
from django.contrib.auth import get_user_model
from board.models import Topic, Newspaper, Comment

User = get_user_model()


class TopicModelTests(TestCase):

    def test_create_topic(self):
        topic = Topic.objects.create(name="Technology")
        self.assertEqual(topic.name, "Technology")
        self.assertEqual(str(topic), "Technology")


class NewspaperModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="redactor1", password="testpassword"
        )
        self.topic = Topic.objects.create(name="Technology")

    def test_create_newspaper(self):
        newspaper = Newspaper.objects.create(
            title="Tech News", content="Latest updates in technology."
        )
        newspaper.topic.add(self.topic)
        newspaper.redactor.add(self.user)
        self.assertEqual(newspaper.title, "Tech News")
        self.assertEqual(newspaper.content, "Latest updates in technology.")
        self.assertIn(self.topic, newspaper.topic.all())
        self.assertIn(self.user, newspaper.redactor.all())
        self.assertEqual(
            str(newspaper), f"{newspaper.title} {newspaper.publisher_date}"
        )


class CommentModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="redactor1", password="testpassword"
        )
        self.newspaper = Newspaper.objects.create(
            title="Tech News", content="Latest updates in technology."
        )

    def test_create_comment(self):
        comment = Comment.objects.create(
            content="Great article!",
            newspaper=self.newspaper,
            redactor=self.user
        )
        self.assertEqual(comment.content, "Great article!")
        self.assertEqual(comment.newspaper, self.newspaper)
        self.assertEqual(comment.redactor, self.user)
        self.assertEqual(
            str(comment), f"Comment by {self.user.username} on {self.newspaper.title}"
        )
