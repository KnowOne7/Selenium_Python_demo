from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_btn = (By.XPATH, "//button[@class='btn']")
    __error_message = (By.XPATH, "//div[@id='error']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username, password):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_btn)
        # wait = WebDriverWait(self._driver, 10)
        # wait.until(ec.visibility_of_all_elements_located(self.__username_field, self.__password_field))
        # self._driver.find_element(self.__username_field).send_keys(username)
        # self._driver.find_element(self.__password_field).send_keys(password)
        # self._driver.find_element(self.__submit_btn).click()

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, 3)
