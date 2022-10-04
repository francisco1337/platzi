import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge( executable_path = 'msedgedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        # return super().setUp()

    def test_hello_world(cls):
        driver = cls.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(cls):
        driver = cls.driver
        driver.get('https://www.wikipedia.com')


    def tearDownClass(cls) -> None:
        cls.driver.quit()
        # return super().tearDown()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello_world_report'))