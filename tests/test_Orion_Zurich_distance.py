import time

import pytest

from utilities.TestClass import TestClass


class TestThirdTest(TestClass):
    @pytest.mark.usefixtures("setup")
    def test_orion_Ziurich_distance(self):
        test_class_obj = TestClass()
        test_class_obj.konstructor(self.driver, self.wait, self.path, self.action)
        test_class_obj.home_page.maximize_window()
        test_class_obj.home_page.accept_cookies()
        test_class_obj.home_page.open_locations_page()
        test_class_obj.locations_page.is_address_correct()


