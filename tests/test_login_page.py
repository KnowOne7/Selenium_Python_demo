import time
import pytest
from selenium.webdriver.common.by import By


# Open page
class TestPositiveScenarios:

    # @pytest.mark.login
    # @pytest.mark.positive
    def test_positive_login(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login")
        # Type username student into Username field

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()

        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Two similar ways to identify, both XPath and Tag Name
        login_successfully_locator = driver.find_element(By.XPATH, "//h1[@class='post-title']")
        text_locator = driver.find_element(By.TAG_NAME, "h1")

        actual_text = login_successfully_locator.text
        assert actual_text == "Logged In Successfully"

# Two similar ways to identify, both XPath and Link Text
        logout_button_locator = driver.find_element(By.XPATH,
                                                    "//a[@href='https://practicetestautomation.com/practice-test-login/']")
        logout_locator = driver.find_element(By.LINK_TEXT, "Log out")

        assert logout_button_locator.is_displayed()

# time.sleep(5)

# //div[@id='loop-container']//article//h1[@class='post-title']
# /html//div[@id='loop-container']/div/article//a[@href='https://practicetestautomation.com/practice-test-login/']
# Type password Password123 into Password field
# Push Submit button
# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
# Verify button Log out is displayed on the new page

# time.sleep(5)
# /html//input[@id='username']

"""
Test case 1: Positive LogIn test
Open page
Type username student into Username field
Type password Password123 into Password field
Puch Submit button
Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Verify new page contains expected text ('Congratulations' or 'successfully logged in')
Verify button Log out is displayed on the new page

"""
