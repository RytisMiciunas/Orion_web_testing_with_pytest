import time

from page_classes.CareersPage import CareersPage
from variable_values import variables

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver, wait, path):
        self.driver = driver
        self.wait = wait
        self.path = path

    def maximize_window(self):
        self.driver.maximize_window()

    def accept_cookies(self):
        self.driver.find_element(*variables.accept_cookie_button_id).click()

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
