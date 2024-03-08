import time

from variable_values import variables
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver, wait, log):
        self.driver = driver
        self.wait = wait
        self.log = log

    def maximize_window(self):
        self.driver.maximize_window()

    def accept_cookies(self):
        passed = True
        try:
            self.driver.find_element(*variables.accept_cookie_button_id).click()
        except:
            passed = False
        return passed


    def press_on_career_button(self):
        career_button = self.driver.find_element(By.LINK_TEXT, variables.careers_linked_text[1])
        self.wait.until(EC.element_to_be_clickable(career_button))
        career_button.click()

    def open_football_page(self):
        while True:
            try:
                self.driver.find_element(By.PARTIAL_LINK_TEXT, variables.football_page_carousel_linked_text[1]).click()
                break
            except:
                self.driver.find_element(By.CLASS_NAME, variables.next_carousel_option_button_class[1]).click()
                time.sleep(1)

    def open_locations_page(self):
        self.driver.find_element(By.LINK_TEXT, variables.locations_page_button_linked_text[1]).click()

    def is_sign_me_up_button_clickable(self):
        try:
            self.wait.until(EC.element_to_be_clickable((self.driver.find_element(By.ID, variables.sign_me_up_button_id[1]))))
            self.driver.find_element(By.ID, variables.sign_me_up_button_id[1]).click()
            self.log.info("sign me up button in home page is working properly")
            return True
        except:
            self.log.error("sign me up button in home page is not clickable")
            return False

    def is_search_button_clickable(self):

        try:
            self.driver.find_element(By.CLASS_NAME, variables.search_button_class[1]).click()
            self.log.info("search button in home page is working properly")
            return True
        except:
            self.log.error("search button in home page is not clickable")
            return False

    def input_characters_into_email_input(self):
        email_input = self.driver.find_element(*variables.work_email_input_in_home_page_id)
        email_input.send_keys("aaaa")

    def input_correct_email_address_into_email_input(self):
        email_input = self.driver.find_element(*variables.work_email_input_in_home_page_id)
        email_input.send_keys("aaa@aaa.com")

    def input_characters_into_first_name_input(self):
        email_input = self.driver.find_element(*variables.first_name_input_in_home_page_id)
        email_input.send_keys("aaaa")

    def press_sign_me_up_button(self):
        self.driver.find_element(*variables.sign_me_up_button_id).click()
        self.driver.implicitly_wait(3)


    def validate_email_input(self):
        try:
            self.driver.find_element(*variables.work_email_input_validation_in_home_page_id)
            return False
        except:
            return True

    def validate_first_name(self):
        try:
            self.driver.find_element(*variables.first_name_input_validation_in_home_page_id)
            print
            return False
        except:
            return True



