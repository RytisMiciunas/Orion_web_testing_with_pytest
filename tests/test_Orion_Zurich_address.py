import pytest

from utilities.TestClass import TestClass


@pytest.mark.usefixtures("setup")
class TestThirdTest(TestClass):

    @pytest.mark.path
    def test_orion_Ziurich_address(self):
        self.home_page.maximize_window()
        self.home_page.accept_cookies()
        self.home_page.open_locations_page()
        conclution = self.locations_page.is_address_correct()
        assert conclution == True
