import pytest
import os
import os.path

from selenium.common import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver

from variable_values import URL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Logging import LogClass
from page_classes.HomePage import HomePage


class BaseClass(LogClass):
    log: str
    driver: WebDriver
    wait: WebDriverWait
    path: str
    home_page: HomePage
    action: ActionChains

    @pytest.fixture
    def setup(self):

        self.path = os.getcwd()
        log_obj = LogClass()
        self.log = log_obj.get_logger()
        self.driver = self.get_driver()
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.action = ActionChains(self.driver)
        yield
        self.destructor()

    def get_driver(self):
        path_to_driver = self.path + r"\chromedriver.exe"
        try:
            service_obj = Service(executable_path=path_to_driver)
            driver = webdriver.Chrome(service=service_obj)
            driver.get(URL.URL_link)
        except FileNotFoundError as e:
            BaseClass.log.critical(f"Chrome driver not found at: {path_to_driver}. Error: {e}")
        except WebDriverException as e:
            BaseClass.log.critical(f"Error initializing Chrome driver. Error: {e}")
        except Exception as e:
            BaseClass.log.critical(f"An unexpected error occurred: {e}")
        finally:
            return driver

    def destructor(self):
        self.driver.quit()
