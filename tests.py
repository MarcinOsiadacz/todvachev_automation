from selenium import webdriver

from pages.category_page import CategoryPage
from pages.login_page import LoginPage
from pages.credentials import Valid

# Test Setup
browser = webdriver.Chrome()
expected_category_options = [
    'Select Category', 'Actions  (1)', 'Selectors  (5)', 'Special Elements  (5)',
    'Tabs and Windows  (1)', 'Test Cases  (3)', 'Test Scenarios  (2)']

# Items in Category Drop Down Menu test

category_page = CategoryPage(driver=browser)
category_page.go()

assert category_page.category_dropdown.options == expected_category_options

# Login Form test

login_page = LoginPage(driver=browser)
login_page.go()

input()
login_page.username_input.input_text(Valid.Username().four_characters())
login_page.password_input.input_text("test1")
login_page.repeat_password_input.input_text("test1")
login_page.login_button.click()

input()
browser.quit()
