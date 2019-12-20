from django.test import TestCase


class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 3)

    def test_good_math(self):
        self.assertEqual(1 + 2, 3)
