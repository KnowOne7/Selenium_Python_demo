import time

import pytest

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenariosPOM:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error",
                             [("incorrectuser", "Password123", "Your username is invalid!"),
                              ("student", "passw0rd", "Your password is invalid!")])
    def test_negative_pom(self, driver, username, password, expected_error):

        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error, "Error message is not expected"



