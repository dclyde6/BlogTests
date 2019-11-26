# Matthew Quaas
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# This will test the login functionality
class HeyStack_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # Remember to create the account for user and pwd before running, otherwise it won't work

    def test_site(self):
        # change this value to the desired username
        user = "instructor"
        # change this value to the desired password for the above user name
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
