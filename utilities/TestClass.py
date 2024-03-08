import pytest

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from page_classes.CareersPage import CareersPage
from page_classes.FootballPage import FootballPage
from page_classes.HomePage import HomePage
from page_classes.LocationsPage import LocationsPage
from page_classes.PossibleJobPositionsPage import PossibleJobPositionsPage
from page_classes.SeniorTestAutomationEngineerPage import SeniorTestAutomationEngineer
from variable_values import URL


class TestClass:
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
    action: ActionChains

    @pytest.fixture(autouse=True)
    def constructor(self, driver, wait, path, action, log):
        self.driver = driver
        self.wait = wait
        self.path = path
        self.log = log
        self.action = action

        self.home_page = HomePage(self.driver, self.wait, self.log)
        self.careers_page = CareersPage(self.driver)
        self.possible_job_positions_page = PossibleJobPositionsPage(self.driver, self.wait)
        self.senior_test_automation_engineer_page = SeniorTestAutomationEngineer(self.driver, self.wait, self.path,
                                                                                 self.log)
        self.football_page = FootballPage(self.driver, self.wait, self.log)
        self.locations_page = LocationsPage(self.driver, self.action)

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver.get(URL.URL_link)
        self.home_page.maximize_window()
        self.home_page.accept_cookies()
        yield
        self.driver.quit()


