import pytest
from Logging import LogClass


from page_classes.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.TestClass import TestClass


class TestFirstTest(TestClass):
    @pytest.mark.usefixtures("setup")
    def test_orion_applying_to_job(self):
        test_class_obj = TestClass()
        test_class_obj.konstructor(self.driver, self.wait, self.path)
        test_class_obj.home_page.maximize_window()
        test_class_obj.home_page.accept_cookies()
        test_class_obj.home_page.press_on_career_button()
        test_class_obj.careers_page.open_location_dropbox()
        test_class_obj.careers_page.select_vilnius_in_dropbox()
        test_class_obj.careers_page.open_category_dropbox()
        test_class_obj.careers_page.select_sales_in_dropbox()
        test_class_obj.careers_page.search_for_job_position()
        test_class_obj.possible_job_positions_page.select_technology_and_engineering_checkbox()
        test_class_obj.possible_job_positions_page.select_senior_test_automation_engineer_position()
        test_class_obj.senior_test_automation_engineer_page.open_frame()
        test_class_obj.senior_test_automation_engineer_page.fill_all_information_into_form()
        test_class_obj.senior_test_automation_engineer_page.click_policy_checkbox()
        test_class_obj.senior_test_automation_engineer_page.submit_form()

