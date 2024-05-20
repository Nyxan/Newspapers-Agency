from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from board.models import Topic, Newspaper, Comment
from accounts.models import Redactor


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)
        self.redactor = Redactor.objects.create(username='redactor1', email='redactor1@example.com')
        self.topic = Topic.objects.create(name='Test Topic')
        self.newspaper = Newspaper.objects.create(title='Test Newspaper', content='Test Content')

    def test_index_view(self):
        url = reverse('board:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/index.html')

    def test_redactor_detail_view(self):
        url = reverse('board:redactor-detail', kwargs={'pk': self.redactor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/redactor_detail.html')

    def test_redactor_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('board:redactor-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/redactor_form.html')

    def test_redactor_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('board:redactor-delete', kwargs={'pk': self.redactor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/redactor_confirm_delete.html')

    def test_topic_detail_view(self):
        url = reverse('board:topic-detail', kwargs={'pk': self.topic.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/topic_detail.html')


    def test_topic_list_view(self):
        url = reverse('board:topic-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/topic_list.html')


    def test_newspaper_list_view(self):
        url = reverse('board:newspaper-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/newspaper_list.html')

    def test_newspaper_detail_view(self):
        url = reverse('board:newspaper-detail', kwargs={'pk': self.newspaper.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/newspaper_detail.html')
