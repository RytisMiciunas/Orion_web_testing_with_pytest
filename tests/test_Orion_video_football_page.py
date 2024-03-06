import time

import pytest
import os
import sys
import os.path

from selenium.webdriver.common.by import By

from utilities.TestClass import TestClass
from variable_values import URL, variables

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Logging import LogClass


class TestSecoundTest(TestClass):
    @pytest.mark.usefixtures("setup")
    def test_orion_play_video(self):
        test_class_obj = TestClass()
        test_class_obj.konstructor(self.driver, self.wait, self.path, self.action)
        test_class_obj.home_page.maximize_window()
        test_class_obj.home_page.accept_cookies()
        test_class_obj.home_page.open_football_page()
        test_class_obj.football_page.open_frame()
        test_class_obj.football_page.press_full_screen()
        test_class_obj.football_page.press_play_button()
        time.sleep(5)
        test_class_obj.football_page.check_is_video_playing()

