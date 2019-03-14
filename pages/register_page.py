from selenium.webdriver.common.by import By


from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class RegisterPage(BasePage):

    url = 'http://testing.todvachev.com/test-scenarios/register-form/'

    @property
    def user_id_input(self):
        locator = Locator(by=By.NAME, value='userid')
        return BaseElement(self.driver, locator)

    @property
    def password_input(self):
        locator = Locator(by=By.NAME, value='passid')
        return BaseElement(self.driver, locator)

    @property
    def name_input(self):
        locator = Locator(by=By.NAME, value='username')
        return BaseElement(self.driver, locator)

    @property
    def country_selection_dropdown(self):
        locator = Locator(by=By.CSS_SELECTOR, value='select[name="country"]')
        return BaseElement(self.driver, locator)

    @property
    def address_input(self):
        locator = Locator(by=By.NAME, value='address')
        return BaseElement(self.driver, locator)

    @property
    def zip_code_input(self):
        locator = Locator(by=By.NAME, value='zip')
        return BaseElement(self.driver, locator)

    @property
    def email_input(self):
        locator = Locator(by=By.NAME, value='email')
        return BaseElement(self.driver, locator)

    @property
    def male_checkbox(self):
        locator = Locator(by=By.XPATH, value='//input[@value="Male"]')
        return BaseElement(self.driver, locator)

    @property
    def female_checkbox(self):
        locator = Locator(by=By.XPATH, value='//input[@value="Female"]')
        return BaseElement(self.driver, locator)

    @property
    def language_checkbox(self):
        locator = Locator(by=By.NAME, value='languageQuestion')
        return BaseElement(self.driver, locator)

    @property
    def about_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='textarea#desc')
        return BaseElement(self.driver, locator)

    @property
    def register_button(self):
        locator = Locator(by=By.XPATH, value='//input[@value="REGISTER"]')
        return BaseElement(self.driver, locator)

    def country_select_usa(self):
        dropdown = self.country_selection_dropdown
        dropdown.select_option_by_value('AD')
        return None

    def no_country_selected(self):
        dropdown = self.country_selection_dropdown
        dropdown.select_option_by_value('Default')
        return None
