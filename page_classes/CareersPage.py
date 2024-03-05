from selenium.webdriver.common.by import By
from page_classes.PossibleJobPositionsPage import PossibleJobPositionsPage
from variable_values import variables


class CareersPage:
    def __init__(self, driver, wait, path):
        self.driver = driver
        self.wait = wait
        self.path = path

    def open_location_dropbox(self):
        self.driver.find_element(*variables.location_dropbox_xpath).click()

    def select_vilnius_in_dropbox(self):
        self.driver.find_element(*variables.selecting_vilnius_xpath).click()

    def open_category_dropbox(self):
        self.driver.find_element(*variables.category_drop_box_xpath).click()

    def select_sales_in_dropbox(self):
        self.driver.find_element(*variables.selecting_sales_xpath).click()

    def search_for_job_position(self):
        # self.driver.find_element(*variables.search_for_jobs_button_id).click()
        self.driver.find_element(*variables.search_for_jobs_button_xpath).click()
