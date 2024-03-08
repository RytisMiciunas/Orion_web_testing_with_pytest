import pytest

from utilities.TestClass import TestClass


@pytest.mark.usefixtures("setup")
class TestFirstTest(TestClass):

    @pytest.mark.path
    def test_orion_applying_to_job(self):
        self.home_page.press_on_career_button()
        self.careers_page.open_location_dropbox()
        self.careers_page.select_vilnius_in_dropbox()
        self.careers_page.open_category_dropbox()
        self.careers_page.select_sales_in_dropbox()
        self.careers_page.search_for_job_position()
        self.possible_job_positions_page.select_technology_and_engineering_checkbox()
        self.possible_job_positions_page.select_senior_test_automation_engineer_position()
        self.senior_test_automation_engineer_page.open_frame()
        self.senior_test_automation_engineer_page.fill_all_information_into_form()
        self.senior_test_automation_engineer_page.click_policy_checkbox()
        conclution = self.senior_test_automation_engineer_page.submit_form()
        assert conclution == True
