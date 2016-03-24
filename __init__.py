
from selenium import webdriver
#import Login
class TestReq():

    def test_tools(self):
        self.driver = webdriver.Firefox()
        self.registration()
       # Login().login_test

    def registration(self):
        driver = self.driver
        driver.get("http://booya.test02.m3v.us")
        sign_up = self.driver.find_element_by_xpath(".//*[@id='top-bar-main']/section/ul/li[6]/a")
        sign_up.click()
        first_name_field = driver.find_element_by_xpath(".//*[@id='user_fname']")
        first_name_field.send_keys("test_1")
        last_name_field = driver.find_element_by_xpath(".//*[@id='user_lname']")
        last_name_field.send_keys("test_2")
        email_field = driver.find_element_by_xpath(".//*[@id='user_email']")
        email_field.send_keys("test+16@gg.gg")
        password_field = driver.find_element_by_xpath(".//*[@id='user_password']")
        password_field.send_keys("qwerty123")
        password_field_confirm = driver.find_element_by_xpath(".//*[@id='user_password_confirmation']")
        password_field_confirm.send_keys("qwerty123")
        """sign_up_button = driver.find_element_by_xpath(".//*[@id='form-signup']/div[3]/div/a")
        sign_up_button.click()
        assert "pick your plan" in 'Booya Fitness'"""




    def tearDown(self):
        self.driver.close()


