import unittest
from click import password_option
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select


class CompareProducts(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Edge("msedgedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        alert = driver.switch_to_alert()
        alert_text = alert.text

        alert.accept()


        


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