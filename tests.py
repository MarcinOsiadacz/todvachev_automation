from selenium import webdriver

from pages.category_page import CategoryPage
from pages.login_page import LoginPage
from pages.credentials import Valid
from pages.credentials import Invalid

# Test Setup
browser = webdriver.Chrome()

# Items in Category Drop Down Menu test case
expected_category_options = [
    'Select Category', 'Actions  (1)', 'Selectors  (5)', 'Special Elements  (5)',
    'Tabs and Windows  (1)', 'Test Cases  (3)', 'Test Scenarios  (2)']

category_page = CategoryPage(driver=browser)
category_page.go()

assert category_page.category_dropdown.dropdown_options == expected_category_options

# Login Form
expected_button_text = 'LOGIN'
expected_incorrect_username_alert = 'User Id should not be empty / length be between 5 to 12'
expected_incorrect_password_alert = 'Password should not be empty / length be between 5 to 12'
expected_different_passwords_alert = 'Passwords do not match!'
expected_successful_login_alert = 'Succesful login!'

login_page = LoginPage(driver=browser)
login_page.go()

# Login Button in Login Form test case
assert login_page.login_button.get_text == expected_button_text

# Username Field in Login Form test case
login_page.username_input.enter_text(Invalid.Username.thirteen_characters())
assert login_page.username_input.get_text == Invalid.Username.thirteen_characters()
login_page.login_button.click()

assert login_page.is_alert_present()
assert login_page.browser_alert.text == expected_incorrect_username_alert
login_page.browser_alert.accept()

login_page.username_input.clear()

# Test Scenario

# Username field with less than 5 characters and correct password (invalid login)
login_page.username_input.enter_text(Invalid.Username().four_characters())
login_page.password_input.enter_text(Valid.password())
login_page.repeat_password_input.enter_text(Valid.password())
login_page.login_button.click()

assert login_page.browser_alert.text == expected_incorrect_username_alert
login_page.browser_alert.accept()

# Username field with more than 12 characters and correct password (invalid login)
login_page.username_input.clear()
login_page.username_input.enter_text(Invalid.Username().thirteen_characters())
login_page.login_button.click()

assert login_page.browser_alert.text == expected_incorrect_username_alert
login_page.browser_alert.accept()

# Username field with 5-12 characters and incorrect password (invalid login)
login_page.username_input.clear()
login_page.password_input.clear()
login_page.repeat_password_input.clear()

login_page.username_input.enter_text(Valid.username())
login_page.password_input.enter_text(Invalid.Password.four_characters())
login_page.repeat_password_input.enter_text(Invalid.Password.four_characters())
login_page.login_button.click()

assert login_page.browser_alert.text == expected_incorrect_password_alert
login_page.browser_alert.accept()

# Correct Username and two different passwords (invalid login)
login_page.password_input.clear()
login_page.repeat_password_input.clear()

login_page.password_input.enter_text(Valid.password())
login_page.repeat_password_input.enter_text(Invalid.Password.four_characters())
login_page.login_button.click()

assert login_page.browser_alert.text == expected_different_passwords_alert
login_page.browser_alert.accept()

# Username field with correct login credentials (valid login)
login_page.password_input.clear()
login_page.repeat_password_input.clear()

login_page.password_input.enter_text(Valid.password())
login_page.repeat_password_input.enter_text(Valid.password())
login_page.login_button.click()

assert login_page.browser_alert.text == expected_successful_login_alert
login_page.browser_alert.accept()

browser.quit()
