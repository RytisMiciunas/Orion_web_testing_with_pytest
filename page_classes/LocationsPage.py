import time


from selenium.webdriver.common.by import By

from variable_values import variables, URL


class LocationsPage:
    def __init__(self, driver, wait, path, log, action):
        self.driver = driver
        self.wait = wait
        self.path = path
        self.log = log
        self.action = action

    def get_Ziurich_map_button_url(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH, variables.open_map_button_xpath[1])).perform()
        return self.driver.find_element(By.XPATH, variables.open_map_button_xpath[1]).get_attribute('href')


    def is_address_correct(self):
        if URL.Zurich_link_should_contain in self.get_Ziurich_map_button_url():
            self.log.info("Address indeed correct")
        else:
            self.log.error("better luck next time :v")
