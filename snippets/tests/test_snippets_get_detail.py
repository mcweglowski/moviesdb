from django.test import TestCase
# from rest_framework.request import Request
# from snippets.models import Snippet


class SnippetGetDetailTest(TestCase):
    # def test_view_returns_snippet_details(self):
    #     snippet = Snippet()
    #     snippet.code = "some code"
    #     snippet.save()

    #     response = self.client.get(f'/snippets/{snippet.pk}',
    #                                follow=True)

    #

    def test_view_creates_snippet(self):
        response = self.client.post('/snippets/', {'code': '123'},
                                    format='json')

        self.assertEqual(response.status_code, 201)
