from Pages.base_page import BasePage
from Pages.Locators import locators_home_page as locator_1
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_attribute(locator_1.all_brands_button))
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://av.by/')

    def cookies_window_close(self):
        return self.find(locator_1.cookies).click()

    # Скрол
    def scroll(self):
        return self.driver.execute_script(f"window.scrollTo(0, {locator_1.scroll_all_brands});")

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

    def dropdown_bmw_click(self):
        return self.find(locator_1.dropdown_bmw).click()

# Нужно настроить ожид
    def filter_search_button_click(self, atr, text):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_attribute
            (
                locator_1.filter_search_button,
                atr,
                text
            )
        )
        return self.find(locator_1.filter_search_button).click()

    def dodge_button_click(self):
        return self.find(locator_1.dodge_button).click()

    def sort_button_click(self):
        return self.find(locator_1.dropdown_sort)

    def sort_button_min_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.dropdown_sort))
        return self.find(locator_1.dropdown_sort_min).click()

    def price_usd(self):
        return self.find(locator_1.price_usd).text

    def login_button(self):
        return self.find(locator_1.login_button).click()

    def register_button(self):
        return self.find(locator_1.register_button).click()

    def register_mail_button(self):
        WebDriverWait(
            self.driver, 10
        ).until(
            EC.text_to_be_present_in_element
            (
                locator_1.register_mail_button,
                'почте'
            )
        )
        return self.find(locator_1.register_mail_button).click()

    def fill_name_field(self, value):
        return self.find(locator_1.name_field).send_keys(value)

    def fill_mail_field(self, value):
        return self.find(locator_1.mail_field).send_keys(value)

    def fill_password_field(self, value):
        return self.find(locator_1.password_fild).send_keys(value)

    def click_checkbox_personal_information(self):
        return self.find(locator_1.checkbox_personal_information).click()

    def click_register_button(self):
        return self.find(locator_1.register_oneself_button).click()

    def name_error_message(self):
        return self.find(locator_1.name_error_message).text

    def mail_error_message(self):
        return self.find(locator_1.mail_error_message).text

    def password_error_message(self):
        return self.find(locator_1.password_error_message).text

