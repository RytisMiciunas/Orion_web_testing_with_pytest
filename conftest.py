import pytest
import os
import sys
import os.path
from variable_values import URL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Logging import LogClass




@pytest.fixture(scope="class")
def setup2(request):
    service_obj = Service(r"C:\Users\rmiciun\source\repos\PycharmProjects\PythonTesting\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.orioninc.com")
    request.cls.driver = driver
    yield
    driver.quit()
