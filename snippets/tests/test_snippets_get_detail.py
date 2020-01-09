from django.test import TestCase
from rest_framework.test import APIRequestFactory
from snippets.models import Snippet
from snippets.views import SnippetDetail


class SnippetGetDetailTest(TestCase):
    def test_view_get_snippet(self):
        snippet = Snippet()
        snippet.code = "some code"
        snippet.save()

        response = self.client.get(f'/snippets/', {'pk': snippet.pk},
                                   follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_put_snippet(self):
        expected_code = 'print("Hello World!")'

        factory = APIRequestFactory()
        request = factory.put('/snippets/1', {'code': expected_code})
        tested_view = SnippetDetail.as_view()

        response = tested_view(request)

        self.assertEqual(response.status_code, 201)

    def test_view_delete_snippet(self):
        snippet = Snippet()
        snippet.code = 'foo="bar"\n'
        snippet.save()

        is_snippet = Snippet.objects.filter(pk=snippet.pk).exists()
        self.assertTrue(is_snippet)

        factory = APIRequestFactory()
        request = factory.delete(f'/snippets/', format='json')

        tested_view = SnippetDetail.as_view()
        response = tested_view(request, pk=snippet.pk)

        is_snippet = Snippet.objects.filter(pk=snippet.pk).exists()

        self.assertEqual(response.status_code, 204)
        self.assertFalse(is_snippet)
