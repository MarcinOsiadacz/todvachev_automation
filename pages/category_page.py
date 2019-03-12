from selenium.webdriver.common.by import By

from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class CategoryPage(BasePage):

    url = "http://testing.todvachev.com/test-cases/items-in-category-drop-down-menu/"

    @property
    def category_dropdown(self):
        locator = Locator(By.CSS_SELECTOR, 'select#cat')
        return BaseElement(self.driver, locator=locator)

