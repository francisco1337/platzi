import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://demo-store.seleniumacademy.com/')



    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main(verbosity = 2)