# ! Open Browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# time.sleep(5)
# Go to Webpage
# driver.get("https://Google.com")

print("Michael")
# Open page
driver.get("https://practicetestautomation.com/practice-test-login")


# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")
# time.sleep(0)

password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
# time.sleep(0)

submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

actual_url = driver.current_url
print(actual_url)
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
print(actual_url == "https://practicetestautomation.com/logged-in-successfully/")

# Two similar ways to identify, both XPath and Tag Name
login_successfully_locator = driver.find_element(By.XPATH, "//h1[@class='post-title']")
text_locator = driver.find_element(By.TAG_NAME, "h1")

actual_text = login_successfully_locator.text
print(actual_text)
assert actual_text == "Logged In Successfully"

# Two similar ways to identify, both XPath and Link Text
logout_button_locator = driver.find_element(By.XPATH, "//a[@href='https://practicetestautomation.com/practice-test-login/']")
logout_locator = driver.find_element(By.LINK_TEXT, "Log out")

assert logout_locator.is_displayed()

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