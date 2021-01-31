import unittest
from selenium import webdriver
from pages.download_page import DownloadPage
import time
import os.path


class DownloadTest(unittest.TestCase):

    downloaded_file_path = 'C:\\Users\\Deniz\\Downloads\\IEDriverServer_Win32_3.10.0.zip'

    # This launches the chrome webdriver and sets it to the variable "driver"
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_previous_releases(self):
        # Tests if the "previous releases" container in the downloads page exists
        driver = self.driver
        download_page = DownloadPage()
        driver.get(download_page.DOWNLOAD_PAGE_URL)
        element = driver.find_element_by_xpath(download_page.PREVIOUS_RELEASES_BUTTON_XPATH)
        element.click()
        element = driver.find_element_by_xpath(download_page.RELEASES_CONTAINER_XPATH)
        assert element

        # This expands the "3.10" dropdown
        element = driver.find_element_by_xpath(download_page.EXPAND_BUTTON_XPATH)
        element.click()

        # This checks if the "3.10" dropdown is shown
        element = driver.find_element_by_xpath(download_page.EXPAND_DIV_XPATH)
        assert "show" not in element.get_attribute("class").split()
        element = driver.find_element_by_xpath(download_page.COLLAPSE_DIV_XPATH)
        assert "show" in element.get_attribute("class").split()
        element = driver.find_element_by_xpath(download_page.RELEASE_DATA_DIV_XPATH)
        assert "show" in element.get_attribute("class").split()

        # This downloads a file from the "3.10" dropdown
        element = driver.find_element_by_xpath(download_page.DOWNLOAD_LINK_XPATH)
        element.click()
        time_to_wait = 10
        time_counter = 0
        # And we check if the file has been downloaded
        while not os.path.exists(self.downloaded_file_path):
            time.sleep(1)
            time_counter += 1
            if time_counter > time_to_wait: break
        assert os.path.isfile(self.downloaded_file_path)

    def tearDown(self):
        # We close the browser and delete the file downloaded when the test is finished
        self.driver.close()
        if os.path.exists(self.downloaded_file_path):
            os.remove(self.downloaded_file_path)


if __name__ == "__main__":
    unittest.main()
