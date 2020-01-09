from django.test import TestCase
from rest_framework.test import APIRequestFactory
from snippets.models import Snippet
from snippets.views import SnippetDetail


class SnippetGetDetailTest(TestCase):
    def setUp(self):
        self.snippet = Snippet()
        self.snippet.code = 'print("Hello World!")'
        self.snippet.save()

    def test_view_get_snippet(self):
        response = self.client.get(f'/snippets/', {'pk': self.snippet.pk},
                                   follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_put_snippet(self):
        expected_code = 'foo="bar"'

        factory = APIRequestFactory()
        request = factory.put('/snippets/', {'code': expected_code})
        tested_view = SnippetDetail.as_view()

        response = tested_view(request, pk=self.snippet.pk)
        snippet = Snippet.objects.get(pk=self.snippet.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(snippet.code, expected_code)

    def test_view_delete_snippet(self):
        is_snippet = Snippet.objects.filter(pk=self.snippet.pk).exists()
        self.assertTrue(is_snippet)

        factory = APIRequestFactory()
        request = factory.delete(f'/snippets/', format='json')

        tested_view = SnippetDetail.as_view()
        response = tested_view(request, pk=self.snippet.pk)

        is_snippet = Snippet.objects.filter(pk=self.snippet.pk).exists()

        self.assertEqual(response.status_code, 204)
        self.assertFalse(is_snippet)
