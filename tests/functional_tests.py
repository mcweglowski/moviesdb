from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_webpage_start_smoke_pass(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Movies DB', self.browser.title)

    def test_can_webpage_start_smoke_fail(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Movies DB2', self.browser.title)


if __name__ == '__main__':
    unittest.main()