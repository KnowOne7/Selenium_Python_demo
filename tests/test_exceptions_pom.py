import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.exceptions_page import ExceptionsPage


class TestExceptionsPOM:

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_exceptions_pom(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row_2_displayed(), "\nRow 2 input should be displayed, but it's not."
        time.sleep(10)

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_element_not_interactable_pom(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_second_food("Sushi")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not expected"
        time.sleep(10)

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_invalid_element_state_exception_pom(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row_1_input("Spaghetti")
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Row was supposed to save but didn't"

        time.sleep(10)

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_invalid_element_state_exception_pom(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instructions_displayed(), "instructions are still displayed"

        time.sleep(10)

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row_2_displayed(), "Confirmation message is not expected"
        time.sleep(10)