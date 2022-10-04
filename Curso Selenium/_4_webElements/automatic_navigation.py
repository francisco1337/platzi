import unittest
from click import password_option
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from time import sleep

class NavigationTest(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Edge("msedgedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://google.com/")


    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys("MICHIS")
        search_field.submit()

        sleep(3)
        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        
        

        


    def tearDown(self) -> None:
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity = 2)