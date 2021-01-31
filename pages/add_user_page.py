class AddUserPage():

    # Page selectors
    USERNAME_XPATH = '//input[@name="username"]'
    PASSWORD_XPATH = '//input[@name="password"]'
    SAVE_BUTTON_XPATH = '//input[@name="FormsButton2"]'
    ADD_USER_INFO_XPATH = '//blockquote/b[text()="The username:"]/..'
    ADD_USER_PAGE_URL = "http://thedemosite.co.uk/addauser.php"

    def __init__(self, driver):
        self.driver = driver

    def create_user(self, username, password):
        # A function that creates a user in the webpage
        input_element = self.driver.find_element_by_xpath(self.USERNAME_XPATH)
        input_element.send_keys(username)

        input_element = self.driver.find_element_by_xpath(self.PASSWORD_XPATH)
        input_element.send_keys(password)

        save_button = self.driver.find_element_by_xpath(self.SAVE_BUTTON_XPATH)
        save_button.click()
