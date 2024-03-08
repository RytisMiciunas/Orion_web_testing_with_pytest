import time
import pytest

from utilities.TestClass import TestClass


@pytest.mark.usefixtures("setup")
class TestSecoundTest(TestClass):

    @pytest.mark.path
    def test_orion_play_video(self):
        self.home_page.open_football_page()
        self.football_page.open_frame()
        self.football_page.press_full_screen()
        self.football_page.press_play_button()
        time.sleep(5)
        conclution = self.football_page.check_is_video_playing()
        assert conclution == True
