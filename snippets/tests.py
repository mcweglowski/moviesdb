from django.test import TestCase
import json
from snippets.models import Snippet


# Create your tests here.
class SnippetListViewTest(TestCase):
    number_of_snippets = 4

    @classmethod
    def setUpTestData(cls):
        for snippet_id in range(cls.number_of_snippets):
            Snippet.objects.create(code='Snippet: #{snippet_id}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/snippets/list', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_list_contains_4_elements(self):
        response = self.client.get('/snippets/list', follow=True)
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content)
        self.assertTrue(len(json_content) == self.number_of_snippets)
