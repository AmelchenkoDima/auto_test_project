from Pages.base_page import BasePage
from Pages.Locators import locators_home_page as locator_1
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.all_brands_button))

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://av.by/')

    def click_all_brands_button(self):
        return self.find(locator_1.all_brands_button).click()

    def lexus_button_click(self):
        return self.find(locator_1.lexus_button).click()

    def car_header(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.car_header))
        return self.find(locator_1.car_header).text

    def toyota_button_click(self):
        return self.find(locator_1.toyota_button).click()

    def toyota_gt_button_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.toyota_gt_button))
        return self.find(locator_1.toyota_gt_button).click()

    def brands_dropdown_click(self):
        return self.find(locator_1.dropdown_brands).click()

    def dropdown_alfa_romeo_click(self):
        return self.find(locator_1.dropdown_alfa_romeo).click()

    def filter_search_button_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.filter_search_button))
        return self.find(locator_1.filter_search_button).click()

    def scroll_all_brands_button(self):
        return self.driver.execute_script(f"window.scrollTo(0, {locator_1.scroll_all_brands});")
    # На данном этапе скролл не нужен
