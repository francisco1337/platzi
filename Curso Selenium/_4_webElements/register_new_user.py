import unittest
from click import password_option
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Edge("msedgedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        driver.implicitly_wait(1)
        middle_name = driver.find_element_by_id('middlename')
        driver.implicitly_wait(1)
        last_name = driver.find_element_by_id('lastname')
        driver.implicitly_wait(1)
        email_address = driver.find_element_by_id('email_address')
        driver.implicitly_wait(1)
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        driver.implicitly_wait(1)
        password = driver.find_element_by_id('password')
        driver.implicitly_wait(1)
        confirm_password = driver.find_element_by_id('confirmation')
        self.driver.implicitly_wait(10000)
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(
                first_name.is_enabled() 
            and middle_name.is_enabled()  
            and last_name.is_enabled()  
            and email_address.is_enabled()  
            and news_letter_subscription.is_enabled()  
            and password.is_enabled()  
            and confirm_password.is_enabled()  
            and submit_button.is_enabled() 
            )
        
        first_name.send_keys("Test")
        middle_name.send_keys("Test")
        last_name.send_keys("Test")
        email_address.send_keys("Test")
        news_letter_subscription.send_keys("Test")
        password.send_keys("Test")
        confirm_password.send_keys("Test@gmail.com")
        submit_button.click()





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