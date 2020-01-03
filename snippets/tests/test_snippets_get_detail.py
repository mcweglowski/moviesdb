from django.test import TestCase
from snippets.models import Snippet


class SnippetGetDetailTest(TestCase):
    def test_view_returns_snippet_details(self):
        snippet = Snippet()
        snippet.code = "some code"
        snippet.save()

        response = self.client.get(f'/snippets/', {'pk': snippet.pk},
                                   follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_creates_snippet(self):
        response = self.client.post('/snippets/', {'code': '123'},
                                    format='json')

        self.assertEqual(response.status_code, 201)
