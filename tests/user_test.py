import unittest
from selenium import webdriver
from pages.add_user_page import AddUserPage
from pages.login_page import LoginPage
import time


class UserTest(unittest.TestCase):
    def setUp(self):
        # This launches the chrome webdriver and sets it to the variable "driver"
        self.driver = webdriver.Chrome()

    def test_create_user(self):
        # This creates a user
        driver = self.driver
        add_user_page = AddUserPage(driver)
        driver.get(add_user_page.ADD_USER_PAGE_URL)
        username = "test"
        password = "test1"
        add_user_page.create_user(username, password)
        add_user_info_xpath = driver.find_element_by_xpath(add_user_page.ADD_USER_INFO_XPATH).text.splitlines()
        time.sleep(1)
        # Checks if the user has been created
        assert ("The username: " + username) in add_user_info_xpath[0]
        assert ("The password: " + password) in add_user_info_xpath[1]

    def test_positive_login_user(self):
        # Positive test if the login is correct
        driver = self.driver
        login_page = LoginPage(driver)
        driver.get(login_page.LOGIN_PAGE_URL)
        username = "test"
        password = "test1"
        login_page.login_user(username, password)
        assert ('**Successful Login**' in driver.page_source)

    def test_negative_login_user(self):
        # Negative test for incorrect login
        driver = self.driver
        login_page = LoginPage(driver)
        driver.get(login_page.LOGIN_PAGE_URL)
        username = "test"
        password = "t1345"
        login_page.login_user(username, password)
        assert ('**Failed Login**' in driver.page_source)

    def tearDown(self):
        # This makes the browser close after the tests are finished
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
