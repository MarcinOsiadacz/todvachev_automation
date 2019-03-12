from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def attribute(self, attribute_name):
        attribute = self.web_element.get_attribute(attribute_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

