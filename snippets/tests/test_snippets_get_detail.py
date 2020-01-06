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
        expected_code = 'print("Hello World!")'
        response = self.client.post('/snippets/', {'code': f'{expected_code}'},
                                    format='json')

        response_pk = response.data['id']
        snippet = Snippet.objects.get(pk=response_pk)

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(snippet)
        self.assertEqual(response.data['code'], expected_code)
        self.assertEqual(snippet.code, expected_code)

    # def test_view_delete_snippet(self):
    #     pass
