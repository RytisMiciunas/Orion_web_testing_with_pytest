from variable_values import variables


class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    def open_location_dropbox(self):
        self.driver.find_element(*variables.location_dropbox_xpath).click()

    def select_vilnius_in_dropbox(self):
        self.driver.find_element(*variables.selecting_vilnius_xpath).click()

    def open_category_dropbox(self):
        self.driver.find_element(*variables.category_drop_box_xpath).click()

    def select_sales_in_dropbox(self):
        self.driver.find_element(*variables.selecting_sales_xpath).click()

    def search_for_job_position(self):
        self.driver.find_element(*variables.search_for_jobs_button_xpath).click()
