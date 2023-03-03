import pytest

from page_objects.loggined_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveLoginPOM:
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL not expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected text"
        assert logged_in_page.is_logout_button_displayed, "Logout Button should be visible"
