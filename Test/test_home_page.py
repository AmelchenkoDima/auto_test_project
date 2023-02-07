from Pages.home_page import HomePage
from Pages.Locators import login_field_arguments as arg
from Pages.Locators import cars_attribute as cars
from time import sleep

#Тусты проверки авто
#Тест: 1 авто из закрытого списка
def test_open_car_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.lexus_button_click()
    assert home_cars_page.car_header(cars.lexus_header) == 'Продажа автомобилей Lexus (Лексус) в Беларуси'


#Тест: 1 авто из раскрытого списка
def test_open_car_expanded_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.click_all_brands_button()
    home_cars_page.toyota_button_click()
    assert home_cars_page.car_header(cars.toyota_header) == 'Продажа автомобилей Toyota (Тойота) в Беларуси'


#Тест: Молель авто из списка
def test_open_car_toyota_gt(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.click_all_brands_button()
    home_cars_page.toyota_button_click()
    home_cars_page.scroll()
    home_cars_page.toyota_gt_button_click()
    assert home_cars_page.car_header(cars.toyota_gt_header) == 'Продажа автомобилей Toyota GT 86'


#Тест: 1 авто из выпадающего списка
def test_open_car_dropdown(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click()
    home_cars_page.dropdown_alfa_romeo_click()
    home_cars_page.filter_search_button_click('href', cars.alfa_romeo_header)
    assert home_cars_page.car_header(
        cars.alfa_romeo_header
    ) == 'Продажа автомобилей Alfa Romeo (Альфа Ромео) в Беларуси'


#Тест: Поколение автомобиля
def test_open_car_generation(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click()
    home_cars_page.dropdown_audi_click()
    home_cars_page.model_dropdown_click()
    home_cars_page.model_dropdown_audi_80()
    home_cars_page.generation_dropdown_click()
    home_cars_page.generation_dropdown_audi_80_b4()
    home_cars_page.filter_search_button_click('href', cars.audi)
    assert home_cars_page.car_model() == 'Audi 80 B4'


#Тесты сортировки
#Тест: Минимальная цена
def test_check_min_price(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.dodge_button_click()
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_min_click()
    assert home_cars_page.price_usd(cars.min_price) == '≈ 600 $'


#Тест: Максимальная цена
def test_check_max_price(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click()
    home_cars_page.dropdown_bmw_click()
    home_cars_page.filter_search_button_click('href', cars.bmw)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_max_click()
    assert home_cars_page.price_usd(cars.max_price) == '≈ 281 007 $'


#Тест: Минимальнаый пробег
def test_check_min_mileage(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.filter_search_button_click('href', cars.all)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_min_mileage_click()
    assert home_cars_page.mileage_car(cars.min_mileage) == '1 км'


#Тест: Новые по году выпуска
def test_check_new_cars(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.filter_search_button_click('href', cars.all)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_new_click()
    assert home_cars_page.year_of_manufacture(cars.year_new) == '2023 г.'


#Тест: Старые по году выпуска
def test_check_old_cars(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.filter_search_button_click('href', cars.all)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_old_click()
    assert home_cars_page.year_of_manufacture(cars.year_old) == '1933 г.'


# Тесты регистрации невалидные значения
# Тесты поля имемни
def test_register_invalid_name_numbers(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.numbers)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.name_error_message() == 'Напишите имя кириллицей'


def test_register_invalid_name_english(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.english)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.name_error_message() == 'Напишите имя кириллицей'


def test_register_invalid_name_sql(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.sql)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.name_error_message() == 'Напишите имя кириллицей'


def test_register_invalid_name_china(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.china)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.name_error_message() == 'Напишите имя кириллицей'


def test_register_invalid_name_symbols(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.symbols)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.name_error_message() == 'Напишите имя кириллицей'


def test_register_invalid_name_html(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.html)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.name_error_message() == 'Напишите имя кириллицей'


def test_register_invalid_name_space(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.space)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.name_error_message() == 'Напишите имя кириллицей'


# Тесты поля Электронная почта
def test_register_invalid_mail_dual_mail(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(f'{arg.mail}.@mail.com')
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'Введите почту полностью. Например, info@av.by'


def test_register_invalid_mail_symbols(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(f'{arg.symbols}.@mail.com')
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'Введите почту полностью. Например, info@av.by'


def test_register_invalid_mail_sql(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(f'{arg.sql}.@mail.com')
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'Введите почту полностью. Например, info@av.by'


def test_register_invalid_mail_html(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(f'{arg.html}.@mail.com')
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'Введите почту полностью. Например, info@av.by'


def test_register_invalid_mail_space(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(f'{arg.space}.@mail.com')
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'Введите почту полностью. Например, info@av.by'


#Тест поля пароль
def test_register_invalid_password_less_than_8_characters(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.min_password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'Минимум 8 символов'


def test_register_invalid_password_sql(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.sql)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'В пароле можно использовать только латинские буквы и цифры'


def test_register_invalid_password_space(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.space)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'В пароле можно использовать только латинские буквы и цифры'


def test_register_invalid_password_html(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.html)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'В пароле можно использовать только латинские буквы и цифры'


def test_register_invalid_password_china(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.china_password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'В пароле можно использовать только латинские буквы и цифры'


def test_register_invalid_password_numbers(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.numbers)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'В пароле можно использовать только латинские буквы и цифры'


def test_register_invalid_password_english(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.name)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.english)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()
    assert home_cars_page.mail_error_message() == 'В пароле можно использовать только латинские буквы и цифры'


#Тесты регистрации валидные значения
def test_register_valid_name_space(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.login_button()
    home_cars_page.register_button()
    home_cars_page.register_mail_button()
    home_cars_page.fill_name_field(arg.space)
    home_cars_page.fill_mail_field(arg.mail)
    home_cars_page.fill_password_field(arg.password)
    home_cars_page.click_checkbox_personal_information()
    home_cars_page.click_register_button()


