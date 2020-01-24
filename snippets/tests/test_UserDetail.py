from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from snippets.views import UserViewSet


class UserDetailTest(TestCase):

    def setUp(self):
        self.user = User()
        self.user.username = 'username'
        self.user.save()

        self.factory = APIRequestFactory()
        self.tested_view = UserViewSet.as_view({'get': 'retrieve'})

    def test_get(self):
        request = self.factory.get('/users/', follow=True)
        response = self.tested_view(request, pk=self.user.pk)
        self.assertEqual(response.status_code, 200)
