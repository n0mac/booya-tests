
from selenium import webdriver


class TestTodoMVC():

    def test(self):
        self.driver = webdriver.Firefox()
        self.registration()

    def registration(self):
        driver = self.driver
        driver.get("https://www.booyafitness.com")
        sign_up = self.driver.find_element_by_xpath(".//*[@id='top-bar-main']/section/ul/li[6]/a")
        sign_up.click()
        first_name_field = driver.find_element_by_xpath(".//*[@id='user_fname']")
        first_name_field.send_keys("test_1")
        last_name_field = driver.find_element_by_xpath(".//*[@id='user_lname']")
        last_name_field.send_keys("test_2")
        email_field = driver.find_element_by_xpath(".//*[@id='user_email']")
        email_field.send_keys("test+14@gg.gg")
        password_field = driver.find_element_by_xpath(".//*[@id='user_password']")
        password_field.send_keys("qwerty123")
        password_field_confirm = driver.find_element_by_xpath(".//*[@id='user_password_confirmation']")
        password_field_confirm.send_keys("qwerty123")




    def tearDown(self):
        self.driver.close()


