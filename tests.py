from selenium import webdriver

from pages.category_page import CategoryPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
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

# Register Form Test Scenario

register_page = RegisterPage(driver=browser)
register_page.go()

# Expected results
# Labels
expected_userid_label_txt = 'User id:'
expected_password_label_txt = 'Password:'
expected_name_label_txt = 'Name:'
expected_address_label_txt = 'Address:'
expected_country_selection_label_txt = 'Country:'
expected_zipcode_label_txt = 'ZIP Code:'
expected_email_label_txt = 'Email:'
expected_sex_selection_label_txt = 'Sex:'
expected_english_checkbox_label_txt = 'English:'
expected_about_label_txt = 'About:'

# Alerts
expected_incorrect_userid_alert = 'User Id should not be empty / length be between 5 to 12'
expected_incorrect_passid_alert = 'Password should not be empty / length be between 7 to 12'
expected_incorrect_name_alert = 'Username must have alphabet characters only'
expected_incorrect_address_alert = 'User address must have alphanumeric characters only'
expected_country_not_selected_alert =r'Select your country from the list'
expected_incorrect_zipcode_alert = 'ZIP code must have numeric characters only'
expected_incorrect_email_alert = 'You have entered an invalid email address!'

# Test Ride
# Verifying labels
assert register_page.user_id_label.text == expected_userid_label_txt
assert register_page.password_label.text == expected_password_label_txt
assert register_page.name_label.text == expected_name_label_txt
assert register_page.address_label.text == expected_address_label_txt
assert register_page.country_selection_label.text == expected_country_selection_label_txt
assert register_page.zip_code_label.text == expected_zipcode_label_txt
assert register_page.email_label.text == expected_email_label_txt
assert register_page.sex_selection_label.text == expected_sex_selection_label_txt
assert register_page.english_checkbox_label.text == expected_english_checkbox_label_txt
assert register_page.about_label.text == expected_about_label_txt

# Checking countries in drop down menu
expected_country_dropdown_options = [
    '(Please select a country)', 'Australia', 'Canada', 'India', 'Russia', 'USA']

assert register_page.country_dropdown.dropdown_options == expected_country_dropdown_options

# Checking if radio and checkbox inputs are clickable
assert register_page.male_checkbox.is_clickable
assert register_page.female_checkbox.is_clickable
assert register_page.english_checkbox.is_clickable


register_page.user_id_input.enter_text(Valid.username())
register_page.password_input.enter_text(Valid.password())
register_page.name_input.enter_text(Valid.username())
register_page.address_input.enter_text(Valid.name())
register_page.country_select_usa()
register_page.zip_code_input.enter_text(Valid.zip_code())
register_page.email_input.enter_text(Valid.email())
register_page.male_checkbox.click()
register_page.english_checkbox.click()
register_page.register_button.click()


input()
browser.quit()
