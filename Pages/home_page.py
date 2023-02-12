from Pages.base_page import BasePage
from Pages.Locators import locators_home_page as locator_1
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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

    def car_button_click(self, arg):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(arg))
        return self.find(arg).click()

    def car_header(self, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator_1.car_header, text))
        return self.find(locator_1.car_header).text

    def brands_dropdown_click(self, arg):
        self.find(locator_1.dropdown_brands).click()
        return self.find(arg).click()

    def brands_dropdown_two_click(self, arg):
        self.find(locator_1.dropdown_two_brands).click()
        return self.find(arg).click()

    def model_dropdown_click(self, arg):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_1.dropdown_model))
        self.find(locator_1.dropdown_model).click()
        return self.find(arg).click()

    def model_dropdown_two_click(self, arg):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_1.dropdown_tow_model))
        self.find(locator_1.dropdown_tow_model).click()
        return self.find(arg).click()

    def generation_dropdown_click(self, arg):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_1.dropdown_generation))
        self.find(locator_1.dropdown_generation).click()
        return self.find(arg).click()

    def generation_dropdown_two_click(self, arg):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_1.dropdown_tow_generation))
        self.find(locator_1.dropdown_tow_generation).click()
        return self.find(arg).click()

    def dropdown_body(self, body):
        self.find(locator_1.dropdown_body).click()
        return self.find(body).click()

    def dropdown_body_two(self, body1=None, body2=None):
        self.find(locator_1.dropdown_body).click()
        self.find(body1).click()
        return self.find(body2).click()

    def dropdown_body_four(self, body1=None, body2=None, body3=None, body4=None):
        self.find(locator_1.dropdown_body).click()
        self.find(body1).click()
        self.find(body2).click()
        self.find(body3).click()
        return self.find(body4).click()

    def dropdown_engine_type(self, engine):
        self.find(locator_1.dropdown_engine_type).click()
        self.find(engine).click()
        return self.find(locator_1.dropdown_engine_type).click()

    def dropdown_engine_type_two(self, engine1=None, engine2=None):
        self.find(locator_1.dropdown_engine_type).click()
        self.find(engine1).click()
        self.find(engine2).click()
        return self.find(locator_1.dropdown_engine_type).click()

    def dropdown_engine_type_four(self, engine1=None, engine2=None, engine3=None, engine4=None):
        self.find(locator_1.dropdown_engine_type).click()
        self.find(engine1).click()
        self.find(engine2).click()
        self.find(engine3).click()
        self.find(engine4).click()
        return self.find(locator_1.dropdown_engine_type).click()

    def add_filter(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.add_filter_button))
        return self.find(locator_1.add_filter_button).click()

    def dropdown_from_year_of_car_manufacture(self, arg):
        self.find(locator_1.dropdown_from_year).click()
        return self.find(arg).click()

    def dropdown_until_year_of_car_manufacture(self, arg):
        self.find(locator_1.dropdown_until_year).click()
        return self.find(arg).click()

    def car_model(self, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator_1.car_model, text))
        return self.find(locator_1.car_model).text

    def cars_model(self):
        return self.find(locator_1.car_model).text

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

    def search_button_active_filter_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.search_button_active_filter))
        return self.find(locator_1.search_button_active_filter).click()

    def delete_filter_car(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.delete_filter_button))
        return self.find(locator_1.delete_filter_button).click()

    def sort_button_click(self):
        return self.find(locator_1.dropdown_sort).click()

    def sort_button_min_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.dropdown_sort_min))
        return self.find(locator_1.dropdown_sort_min).click()

    def sort_button_max_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.dropdown_sort_max))
        return self.find(locator_1.dropdown_sort_max).click()

    def sort_button_min_mileage_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.dropdown_sort_max))
        return self.find(locator_1.dropdown_sort_min_mileage).click()

    def sort_button_new_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_1.dropdown_sort_max))
        return self.find(locator_1.dropdown_sort_new).click()

    def sort_button_old_click(self):
        return self.find(locator_1.dropdown_sort_old).click()

    def price_usd(self, price):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator_1.price_usd, price))
        return self.find(locator_1.price_usd).text

    def year_of_manufacture(self, year):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator_1.year_of_manufacture, year))
        return self.find(locator_1.year_of_manufacture).text

    def mileage_car(self, mileage):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator_1.mileage, mileage))
        return self.find(locator_1.mileage).text

    def check_params(self, arg):
        car_params = self.find(locator_1.car_params).text
        body = list()
        body.append(arg)
        for word in body:
            if word in car_params:
                return word
        return car_params

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

