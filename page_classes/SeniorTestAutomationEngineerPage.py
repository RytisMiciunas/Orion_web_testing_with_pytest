import time
import Logging
import names

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from variable_values import variables, URL
from faker import Faker
from pynput.keyboard import Key, Controller


class SeniorTestAutomationEngineer:
    def __init__(self, driver, wait, path, log):
        self.driver = driver
        self.wait = wait
        self.path = path
        self.log = log

    def open_frame(self):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, variables.senior_tester_page_frame_name_id[1])))
        except:
            self.log.error("Couldn't open iframe")
        self.wait.until(EC.element_to_be_clickable((By.ID, variables.input_name_id[1])))

    def __get_personal_information(self):
        full_info = names.get_full_name().split()
        full_info.append(full_info[0] + "." + full_info[1] + "@gmail.com")
        fake = Faker("lt_LT")
        full_info.append(fake.phone_number())
        return full_info

    def write_name_into_form(self, name):
        self.driver.find_element(*variables.input_name_id).send_keys(name)

    def write_last_name_into_form(self, last_name):
        self.driver.find_element(*variables.input_last_name_id).send_keys(last_name)

    def write_mail_into_form(self, mail):
        self.driver.find_element(*variables.input_mail_id).send_keys(mail)

    def write_phone_into_form(self, phone):
        self.driver.find_element(*variables.input_phone_id).send_keys(phone)

    def upload_file_into_form(self, file_name, xpath):
        file = self.driver.find_element(*xpath)
        self.wait.until(EC.element_to_be_clickable(file))
        file.click()
        keyboard = Controller()
        time.sleep(2)
        keyboard.type(self.path + file_name)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def fill_all_information_into_form(self):
        personal_info = self.__get_personal_information()
        self.write_name_into_form(personal_info[0])
        self.write_last_name_into_form(personal_info[1])
        self.write_mail_into_form(personal_info[2])
        self.write_phone_into_form(personal_info[3])
        self.upload_file_into_form(URL.cv_path, variables.upload_cv_linked_text_xpath)
        self.upload_file_into_form(URL.cover_letter_path, variables.upload_cover_letter_linked_text_xpath)

    def click_policy_checkbox(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, variables.cover_letter_uploaded_img_id[1])))
        self.driver.find_element(*variables.agree_with_policy_checkbox_xpath).click()

    def submit_form(self):
        self.driver.find_element(*variables.submit_form_button_id).click()
