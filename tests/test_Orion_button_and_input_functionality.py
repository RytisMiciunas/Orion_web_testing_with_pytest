import time

import pytest

from utilities.TestClass import TestClass


@pytest.mark.usefixtures("setup")
class TestFunctionalityTestingClass(TestClass):

    @pytest.mark.button
    def test_home_page_carees_button(self):
        conclution = self.home_page.is_sign_me_up_button_clickable()
        assert conclution == True

    @pytest.mark.button
    def test_home_page_search_button(self):
        conclution = self.home_page.is_search_button_clickable()

        assert conclution == True

    @pytest.mark.input
    def test_home_page_work_email_input_with_characters(self):
        self.home_page.input_characters_into_email_input()
        self.home_page.press_sign_me_up_button()
        conclution = self.home_page.validate_email_input()
        assert conclution == False

    @pytest.mark.input
    def test_home_page_work_email_input_with_correct_email(self):
        self.home_page.input_correct_email_address_into_email_input()
        self.home_page.press_sign_me_up_button()
        conclution = self.home_page.validate_email_input()
        assert conclution == True

    @pytest.mark.input
    def test_home_page_first_name_input(self):
        self.home_page.input_characters_into_first_name_input()
        self.home_page.press_sign_me_up_button()
        conclution = self.home_page.validate_first_name()
        assert conclution == True
