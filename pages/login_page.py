class LoginPage():

    # Page selectors
    USERNAME_XPATH = '//input[@name="username"]'
    PASSWORD_XPATH = '//input[@name="password"]'
    LOGIN_BUTTON_XPATH = '//input[@name="FormsButton2"]'
    LOGIN_PAGE_URL = "http://thedemosite.co.uk/login.php"

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, username, password):
        # A function that logs the user in
        input_element = self.driver.find_element_by_xpath(self.USERNAME_XPATH)
        input_element.send_keys(username)

        input_element = self.driver.find_element_by_xpath(self.PASSWORD_XPATH)
        input_element.send_keys(password)

        login_button = self.driver.find_element_by_xpath(self.LOGIN_BUTTON_XPATH)
        login_button.click()
