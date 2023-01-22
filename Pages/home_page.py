from Pages.base_page import BasePage
from Pages.Locators import locators_home_page as locator_1


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://av.by/')

    def lexus_open(self):
        self.find(locator_1.lexus_button).click()

    def lexus_page(self):
        self.find(locator_1.lexus_page)

