import time

import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from variable_values import variables


class FootballPage:

    def __init__(self, driver, wait, log):
        self.driver = driver
        self.wait = wait
        self.log = log

    def open_frame(self):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, variables.football_page_iframe[1])))
        except:
            self.log.error("cant connect to frame")

    def press_full_screen(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, variables.football_interview_full_screen_xpath[1])))
            self.driver.execute_script("arguments[0].scrollIntoView();",
                                       (self.driver.find_element(*variables.football_interview_full_screen_xpath)))
            self.driver.find_element(*variables.football_interview_full_screen_xpath).click()
        except:
            self.log.error("Cannot click full screen button")

    def press_play_button(self):
        self.driver.find_element(*variables.football_interview_play_button_class).click()

    def check_is_video_playing(self):
        video_playing_time = self.driver.find_element(*variables.football_interview_time_bar_xpath).get_attribute("aria-valuenow")
        if int(video_playing_time) > 0:
            return True
        else:
            return False



