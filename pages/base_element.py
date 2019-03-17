from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find_element()

    def find_element(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None

    def enter_text(self, text):
        self.web_element.send_keys(text)
        return None

    def clear(self):
        self.web_element.clear()
        return None

    def attribute(self, attribute_name):
        attribute = self.web_element.get_attribute(attribute_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

    @property
    def dropdown_options(self):
        selected_element = Select(self.web_element)
        list_of_options = [element.text for element in selected_element.options]
        return list_of_options

    @property
    def get_text(self):
        text = self.web_element.get_attribute('value')
        return text

    def select_option_by_value(self, value):
        selected_element = Select(self.web_element)
        selected_element.select_by_value(value)
        return None

    def is_clickable(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable())
            element_state = True
        except TimeoutException:
            element_state = False
        return element_state
