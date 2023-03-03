import time

import pytest

from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    # @pytest.mark.login
    # @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error",
                             [("incorrectuser", "Password123", "Your username is invalid!"),
                              ("student", "passw0rd", "Your password is invalid!")])
    def test_negative(self, driver, username, password, expected_error):
        driver.get("https://practicetestautomation.com/practice-test-login")

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        time.sleep(1)

        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should."

        error_message = error_message_locator.text
        assert error_message == expected_error, "Error message is not expected"


    def test_negative_username(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("bob")
        # username_locator.send_keys("student")

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        # time.sleep(2)

        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should."

        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"
        # time.sleep(3)

    def test_negative_password(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password1123")

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        # time.sleep(2)

        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected."


"""

Test case 2: Negative username test
Open page
Type username incorrectUser into Username field
Type password Password123 into Password field
Puch Submit button
Verify error message is displayed
Verify error message text is Your username is invalid!

"""
