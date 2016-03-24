import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class BooyaSignIn(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.sign_in_button_id = "//a[@href='/signin']"
        self.email_field_sign_in_id = ".//*[@id='user_email']"
        self.password_field_sign_in_id = ".//*[@id='user_password']"
        self.sign_in_button_end_id = ".//*[@id='new_user']/div[5]/input"
        self.start_trial_button_id = ".//*[@id='monthly']/a/div[2]/div"
        self.credit_card_field_id = ".//*[@id='card_number']"
        self.cvv_field_id = ".//*[@id='card_code']"
        self.month_picker_id = ".//*[@id='select2-result-label-261']"
        self.year_picker_id = ".//*[@id='select2-drop-mask']"
        self.save_continue_button_id = ".//*[@id='submit-card']"

    def test_search_in_python_org(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.http.phishy-userpass-length', 255)
        driver = webdriver.Firefox(firefox_profile=profile)
        driver.get("https://demo:pass@booyastage.herokuapp.com")
        sign_in = driver.find_element_by_xpath(self.sign_in_button_id)
        sign_in.click()
        email_field_sign_in = driver.find_element_by_xpath(self.email_field_sign_in_id)
        email_field_sign_in.send_keys("test@gg.gg")
        password_field_sign_in = driver.find_element_by_xpath(self.password_field_sign_in_id)
        password_field_sign_in.send_keys("qwerty123")
        sign_in_button = driver.find_element_by_xpath(self.sign_in_button_end_id)
        sign_in_button.click()
        assert "pick your plan" in driver.page_source
        start_trial_button = driver.find_element_by_xpath(self.start_trial_button_id)
        start_trial_button.click()
        credit_card_input = driver.find_element_by_xpath(self.credit_card_field_id)
        credit_card_input.send_keys("4242 4242 4242 4242")
        cvv_input = driver.find_element_by_xpath(self.cvv_field_id)
        cvv_input.send_keys("123")
        month_pick = driver.find_element_by_class_name("select2-container")
        month_pick.click()
        click_month = driver.find_element_by_xpath(".//*[@id='select2-results-3']/li[3]")
        click_month.click()
        year_pick = driver.find_element_by_id("s2id_card_year")
        year_pick.click()
        click_year = driver.find_element_by_xpath(".//*[@id='select2-results-4']/li[2]")
        click_year.click()

        #if click_year == False:
            #print "Success"

        click_save = driver.find_element_by_xpath(self.save_continue_button_id)
        click_save.click()
        assert  "Complete Booya Registration" in driver.page_source


        #select = Select(driver.find_element_by_xpath(".//*[@id='card_month']"))
        #select.select_by_value("3")
        #Select(driver.find_element_by_class_name("select2-container")).select_by_value("2")