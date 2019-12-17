from selenium import webdriver
import unittest


class SmokeTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_hompeage_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Movies DB', self.browser.title)


if '__main__' == __name__:
    unittest.main(warnings='ignore')
