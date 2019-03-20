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

# Expected results
expected_incorrect_userid_alert = 'User Id should not be empty / length be between 5 to 12'
expected_incorrect_passid_alert = 'Password should not be empty / length be between 7 to 12'
expected_incorrect_name_alert = 'Username must have alphabet characters only'
expected_incorrect_address_alert = 'User address must have alphanumeric characters only'
expected_country_not_selected_alert = 'Select your country from the list'
expected_country_selected = 'USA'
expected_incorrect_zipcode_alert = 'ZIP code must have numeric characters only'
expected_incorrect_email_alert = 'You have entered an invalid email address!'
example_about = 'Lorem Ipsum Lorem Ipsum, Lorem Ipsum.'
expected_url = 'http://testing.todvachev.com/test-scenarios/register-form/?userid=asdf1&passid=asdf1234%21&username' \
               '=Asdf&address=Street1&country=AD&zip=12345&email=example%40example.com&sex=Male&desc=Lorem+Ipsum' \
               '+Lorem+Ipsum%2C+Lorem+Ipsum.&submit=REGISTER'

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

# All fields empty
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_userid_alert
register_page.browser_alert.accept()

# All Invalid data
# Incorrect user id - shorter than 5 characters
register_page.user_id_input.enter_text(Invalid.UserID.four_characters())
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_userid_alert
register_page.browser_alert.accept()

# Incorrect user id - longer than 12 characters
register_page.user_id_input.clear()
register_page.user_id_input.enter_text(Invalid.UserID.thirteen_characters())
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_userid_alert
register_page.browser_alert.accept()

# Changing to valid user id
register_page.user_id_input.clear()
register_page.user_id_input.enter_text(Valid.user_id())

# Incorrect password - shorter than 7 characters
register_page.password_input.enter_text(Invalid.Password.four_characters())
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_passid_alert
register_page.browser_alert.accept()

# Incorrect password - longer than 12 characters
register_page.password_input.clear()
register_page.password_input.enter_text(Invalid.Password.thirteen_characters())
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_passid_alert
register_page.browser_alert.accept()

# Changing to valid password
register_page.password_input.clear()
register_page.password_input.enter_text(Valid.password())

# Incorrect name (including digits)
register_page.name_input.enter_text(Invalid.Name.with_digits())
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_name_alert
register_page.browser_alert.accept()

# Changing to valid name
register_page.name_input.clear()
register_page.name_input.enter_text(Valid.name())

# Incorrect address
register_page.address_input.enter_text(Invalid.Address.with_special_symbols())
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_address_alert
register_page.browser_alert.accept()

# Changing to valid address
register_page.address_input.clear()
register_page.address_input.enter_text(Valid.address())

# Country not selected
register_page.no_country_selected()
register_page.register_button.click()

assert register_page.browser_alert.text == expected_country_not_selected_alert
register_page.browser_alert.accept()

# Selecting a country
register_page.country_select_usa()
assert register_page.country_selection_dropdown.currently_selected_option_text == \
       expected_country_selected

# Incorrect ZIP Code
# Zip Code with special symbols
register_page.zip_code_input.enter_text(Invalid.ZipCode.with_special_symbols())
register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_zipcode_alert
register_page.browser_alert.accept()

# Zip Code with letters
register_page.zip_code_input.clear()
register_page.zip_code_input.enter_text(Invalid.ZipCode.with_letters())

register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_zipcode_alert
register_page.browser_alert.accept()

# Zip Code with space
register_page.zip_code_input.clear()
register_page.zip_code_input.enter_text(Invalid.ZipCode.with_space())

register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_zipcode_alert
register_page.browser_alert.accept()

# Changing to valid Zip code
register_page.zip_code_input.clear()
register_page.zip_code_input.enter_text(Valid.zip_code())

# Incorrect Email
# No domain
register_page.email_input.enter_text(Invalid.Email.no_domain())

register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_email_alert
register_page.browser_alert.accept()

# No extension
register_page.email_input.clear()
register_page.email_input.enter_text(Invalid.Email.no_extension())

register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_email_alert
register_page.browser_alert.accept()

# No user
register_page.email_input.clear()
register_page.email_input.enter_text(Invalid.Email.no_user())

register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_email_alert
register_page.browser_alert.accept()

# Not at
register_page.email_input.clear()
register_page.email_input.enter_text(Invalid.Email.not_at())

register_page.register_button.click()

assert register_page.browser_alert.text == expected_incorrect_email_alert
register_page.browser_alert.accept()

# Changing to valid Email
register_page.email_input.clear()
register_page.email_input.enter_text(Valid.email())

# Sex, English and About are not obligatory
# Checking Sex selection
register_page.female_checkbox.click()
assert register_page.female_checkbox.is_selected()

register_page.male_checkbox.click()
assert register_page.male_checkbox.is_selected()

# Checking English checkbox
# Checked by default
assert register_page.english_checkbox.is_selected()

# Unchecking English checkbox
register_page.english_checkbox.click()
assert register_page.english_checkbox.is_selected() is not True

# About
register_page.about_input.enter_text(example_about)
assert register_page.about_input.get_text == example_about

# Checking if registration passes
register_page.register_button.click()
assert register_page.do_current_url_matches(expected_url)

# Closing the driver
browser.quit()
