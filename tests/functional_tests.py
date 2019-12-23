from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        selenium_url = 'http://localhost:4444/wd/hub'
        capabilities = DesiredCapabilities.CHROME.copy()

        self.browser = webdriver.Remote(desired_capabilities=capabilities,
                                        command_executor=selenium_url)

        # self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_webpage_start_smoke_pass(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Movies DB', self.browser.title)

    def test_can_webpage_start_smoke_fail(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Movies DB2', self.browser.title)

    def test_dummy_pass(self):
        self.assertEqual(1, 1)

    def test_locate_by_id(self):
        self.browser.get('http://localhost:8000')
        test_form = self.browser.find_element_by_id('testForm')
        self.assertIn('Movies Site!', test_form.text)


if __name__ == '__main__':
    unittest.main()
