import pytest
import os
import os.path

from selenium.common import WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Logging import LogClass


@pytest.fixture
def path():
    return os.getcwd()


@pytest.fixture
def log():
    log_obj = LogClass()
    return log_obj.get_logger()


@pytest.fixture
def driver(path, log):
    try:
        service_obj = Service(executable_path=path + r"\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    except FileNotFoundError as e:
        log.critical(f"Chrome driver not found at: {path}. Error: {e}")
    except WebDriverException as e:
        log.critical(f"Error initializing Chrome driver. Error: {e}")
    except Exception as e:
        log.critical(f"An unexpected error occurred: {e}")
    finally:
        return driver


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=10)


@pytest.fixture
def action(driver):
    return ActionChains(driver)


def pytest_configure(config):
    config.addinivalue_line("markers", "input: this marker indicates that his test is testing input")
    config.addinivalue_line("markers", "button: this marker indicates button testing")
    config.addinivalue_line("markers", "path: this marker indicates going per pages")
