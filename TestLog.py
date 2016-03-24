from selenium import webdriver
import unittest

class BaseTestCase(unittest.TestCase):

        def testlog_1(self):
            self.driver = webdriver.Firefox()
            self.sign_in_button_id = ".//*[@id='top-bar-main']/section/ul/li[5]/a"
            self.email_field_sign_in_id = ".//*[@id='user_email']"
            self.password_field_sign_in_id = ".//*[@id='user_password']"
            self.sign_in_button_end_id = ".//*[@id='new_user']/div[5]/input"
            driver = self.driver
            driver.get("http://booya.test02.m3v.us/")
            sign_in = driver.find_element_by_xpath(self.sign_in_button_id)
            sign_in.click()
            email_field_sign_in = driver.find_element_by_xpath(self.email_field_sign_in_id)
            email_field_sign_in.send_keys("test+14@gg.gg")
            password_field_sign_in = driver.find_element_by_xpath(self.password_field_sign_in_id)
            password_field_sign_in.send_keys("qwerty123")
            sign_in_button = driver.find_element_by_xpath(self.sign_in_button_end_id)
            sign_in_button.click()
            assert "pick your plan" in driver.page_source
            driver.close()



