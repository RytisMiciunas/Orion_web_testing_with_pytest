import time

from selenium.webdriver.common.by import By

from page_classes.SeniorTestAutomationEngineerPage import SeniorTestAutomationEngineer
from variable_values import variables
from selenium.webdriver.support import expected_conditions as EC


class PossibleJobPositionsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def select_technology_and_engineering_checkbox(self):
        self.driver.find_element(*variables.technology_and_engineering_checkbox_xpath).click()
        # self.driver.find_element(By.XPATH, variables.technology_and_engineering_checkbox_xpath[1]).click()


    def select_senior_test_automation_engineer_position(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.PARTIAL_LINK_TEXT, variables.senior_test_automation_engineer_position_linked_text[1])))
        self.driver.find_element(By.PARTIAL_LINK_TEXT, variables.senior_test_automation_engineer_position_linked_text[1]).click()
