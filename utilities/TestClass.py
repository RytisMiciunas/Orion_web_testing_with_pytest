import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Logging import LogClass
from page_classes.CareersPage import CareersPage
from page_classes.FootballPage import FootballPage
from page_classes.HomePage import HomePage
from page_classes.LocationsPage import LocationsPage
from page_classes.PossibleJobPositionsPage import PossibleJobPositionsPage
from page_classes.SeniorTestAutomationEngineerPage import SeniorTestAutomationEngineer
from utilities.BaseClass import BaseClass


class TestClass(BaseClass):
    home_page: HomePage
    careers_page: CareersPage
    possible_job_positions_page: PossibleJobPositionsPage
    senior_test_automation_engineer_page: SeniorTestAutomationEngineer
    football_page: FootballPage
    locations_page: LocationsPage
    driver: WebDriver
    wait: WebDriverWait
    path: str
    log: str

    # @pytest.mark.usefixtures("setup")
    def konstructor(self, driver_var, wait_var, path_var):
        self.driver = driver_var
        self.wait = wait_var
        self.path = path_var
        self.log = LogClass.get_logger(self)

        self.home_page = HomePage(self.driver, self.wait, self.path)
        self.careers_page = CareersPage(self.driver, self.wait, self.path)
        self.possible_job_positions_page = PossibleJobPositionsPage(self.driver, self.wait, self.path)
        self.senior_test_automation_engineer_page = SeniorTestAutomationEngineer(self.driver, self.wait, self.path, self.log)
        self.football_page = FootballPage(self.driver, self.wait, self.path, self.log)
        self.locations_page = LocationsPage(self.driver, self.wait, self.path, self.log)
