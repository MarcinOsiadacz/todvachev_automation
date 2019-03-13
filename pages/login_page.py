from selenium.webdriver.common.by import By


from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class LoginPage(BasePage):

    url = 'http://testing.todvachev.com/test-scenarios/login-form/'

    @property
    def username_input(self):
        locator = Locator(by=By.NAME, value='userid')
        return BaseElement(self.driver, locator)

    @property
    def password_input(self):
        locator = Locator(by=By.NAME, value='passid')
        return BaseElement(self.driver, locator)

    @property
    def repeat_password_input(self):
        locator = Locator(by=By.NAME, value='repeatpassid')
        return BaseElement(self.driver, locator)

    @property
    def login_button(self):
        locator = Locator(by=By.NAME, value='submit')
        return BaseElement(self.driver, locator)
