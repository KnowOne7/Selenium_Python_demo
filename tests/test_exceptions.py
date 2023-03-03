import pytest, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    # @pytest.mark.exceptions
    def test_exceptions(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        driver.find_element(By.XPATH, "//button[@id='add_btn']").click()
        wait = WebDriverWait(driver, 10)

        row_2_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/label[.='Row 2']")))
        assert row_2_element.is_displayed(), "\nRow 2 input should be displayed, but it's not."

    # @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_element_not_interactable(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)

        row_2_element = wait.until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # driver.find_element(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/label[.='Row 2']")

        assert row_2_element.is_displayed(), "\nRow 2 input should be displayed, but it's not."

        row_2_element.send_keys("Tacos")
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@id='save_btn']").click()

        # row_3_element = driver.find_element(By.XPATH, "//div[@id='confirmation']")
        #  double quotes , locator must be tuple.
        row_3_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='confirmation']")))
        # row_3_element = wait.until(ec.presence_of_element_located(("//div[@id='confirmation']")))
        # confirmation_message = row_3_element.text
        # assert confirmation_message == "Row 2 was saved", "\nRow 3 input should be displayed, but it's not."
        # assert row_3_element.is_displayed(), "\nRow 3 input should be displayed, but it's not."
        assert row_3_element.text == "Row 2 was saved", "\nRow 3 input should be displayed, but it's not."

    # @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        driver.find_element(By.XPATH, "//button[@id='edit_btn']").click()

        row1_field = driver.find_element(By.XPATH,
                                         "//div[@id='row1']/input[@class='input-field']")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row1_field))

        row1_field.clear()
        row1_field.send_keys("Salami")

        wait.until(ec.visibility_of_element_located((By.XPATH, "/html//button[@id='save_btn']"))).click()

        confirmation_message = wait.until(ec.visibility_of_element_located((By.XPATH, "/html//div[@id='confirmation']")))
        assert confirmation_message.text == "Row 1 was saved", "Row was supposed to save but didn't"

        time.sleep(10)

    # @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        assert driver.find_element(By.XPATH, "/html//p[@id='instructions']").is_displayed()

        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)

        assert wait.until(ec.invisibility_of_element((By.XPATH, "/html//p[@id='instructions']")), "instructions still displayed")

        time.sleep(10)

    # @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        driver.find_element(By.XPATH, "//button[@id='add_btn']").click()

        # wait = WebDriverWait(driver, 10)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")), "Failed waiting for row 2 visibility")
        time.sleep(10)