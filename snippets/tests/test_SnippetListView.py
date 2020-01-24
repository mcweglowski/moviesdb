from django.contrib.auth.models import User
from django.test import TestCase
import json
from snippets.models import Snippet


class SnippetListViewTest(TestCase):
    number_of_snippets = 4

    def setUp(self):
        user = User()
        user.password = '123'
        user.email = 'email@email.com'
        user.save()

        for snippet_id in range(self.number_of_snippets):
            snippet = Snippet()
            snippet.code = 'Snippet: #{snippet_id}'
            snippet.owner_id = user.pk
            snippet.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/snippets/snippets/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_list_contains_4_elements(self):
        response = self.client.get('/snippets/snippets/', follow=True)
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content)
        self.assertEqual(len(json_content), self.number_of_snippets)