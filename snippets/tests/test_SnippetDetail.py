from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from snippets.models import Snippet
from snippets.views import SnippetDetail


class SnippetDetailTest(TestCase):
    def setUp(self):
        user = User()
        user.password = '123'
        user.email = 'email@email.com'
        user.save()

        self.snippet = Snippet()
        self.snippet.code = 'print("Hello World!")'
        self.snippet.owner_id = user.pk
        self.snippet.save()

        self.factory = APIRequestFactory()
        self.tested_view = SnippetDetail.as_view()

    def test_get(self):
        response = self.client.get(f'/snippets/', {'pk': self.snippet.pk},
                                   follow=True)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        expected_code = 'foo="bar"'

        request = self.factory.put('/snippets/', {'code': expected_code})

        response = self.tested_view(request, pk=self.snippet.pk)
        snippet = Snippet.objects.get(pk=self.snippet.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(snippet.code, expected_code)

    def test_delete(self):
        is_snippet = Snippet.objects.filter(pk=self.snippet.pk).exists()
        self.assertTrue(is_snippet)

        request = self.factory.delete(f'/snippets/', format='json')

        response = self.tested_view(request, pk=self.snippet.pk)

        is_snippet = Snippet.objects.filter(pk=self.snippet.pk).exists()

        self.assertEqual(response.status_code, 204)
        self.assertFalse(is_snippet)
