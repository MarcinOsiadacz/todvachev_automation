from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    @property
    def browser_alert(self):
        alert = Alert(driver=self.driver)
        return alert

    def is_alert_present(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.alert_is_present())
            alert_state = True
        except TimeoutException:
            alert_state = False
        return alert_state


