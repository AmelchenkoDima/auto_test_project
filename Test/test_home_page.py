from Pages.home_page import HomePage
from Pages.Locators import login_field_arguments as arg
from Pages.Locators import cars_attribute_waiting as CAW
from Pages.Locators import locators_cars as cars
from time import sleep


#Тусты проверки авто
#Тест: 1 авто из закрытого списка
def test_open_car_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.car_button_click(cars.lexus)
    assert home_cars_page.car_header(CAW.lexus_header) == 'Продажа автомобилей Lexus (Лексус) в Беларуси'


#Тест: 1 авто из раскрытого списка
def test_open_car_expanded_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.click_all_brands_button()
    home_cars_page.car_button_click(cars.toyota)
    assert home_cars_page.car_header(CAW.toyota_header) == 'Продажа автомобилей Toyota (Тойота) в Беларуси'


#Тест: Молель авто из списка
def test_open_car_toyota_gt(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.click_all_brands_button()
    home_cars_page.car_button_click(cars.toyota)
    home_cars_page.scroll()
    home_cars_page.car_button_click(cars.toyota_gt)
    assert home_cars_page.car_header(CAW.toyota_gt_header) == 'Продажа автомобилей Toyota GT 86'


#Тест: 1 авто из выпадающего списка
def test_open_car_dropdown(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click(cars.alfa_romeo)
    home_cars_page.filter_search_button_click('href', CAW.alfa_romeo)
    assert home_cars_page.car_header(
        CAW.alfa_romeo_header
    ) == 'Продажа автомобилей Alfa Romeo (Альфа Ромео) в Беларуси'


#Тест: Поколение автомобиля
def test_open_car_generation(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click(cars.audi)
    home_cars_page.model_dropdown_click(cars.audi_80)
    home_cars_page.generation_dropdown_click(cars.audi_80_b4)
    home_cars_page.filter_search_button_click('href', CAW.audi)
    assert home_cars_page.car_model(CAW.audi_80_b4) == 'Audi 80 B4'


#Тест: Год выпуска
def test_year_of_car_manufacture(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.scroll()
    home_cars_page.dropdown_from_year_of_car_manufacture()
    sleep(200)


#Тест: Добавление автомобиля в поиск
def test_add_new_filter_car(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click(cars.audi)
    home_cars_page.model_dropdown_click(cars.audi_80)
    home_cars_page.generation_dropdown_click(cars.audi_80_b4)
    home_cars_page.add_filter()
    home_cars_page.brands_dropdown_two_click(cars.bentley)
    home_cars_page.model_dropdown_two_click(cars.bentley_continental_gt)
    home_cars_page.generation_dropdown_two_click(cars.bentley_continental_gt_restyling)
    home_cars_page.filter_search_button_click('href', CAW.audi_bentley)
    assert home_cars_page.cars_model() == 'Audi 80 B4' or 'Bentley Continental GT II · Рестайлинг'


#Тест: Удаление автомобиля из поиска
def test_delete_new_filter_car(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click(cars.audi)
    home_cars_page.model_dropdown_click(cars.audi_80)
    home_cars_page.generation_dropdown_click(cars.audi_80_b4)
    home_cars_page.add_filter()
    home_cars_page.brands_dropdown_two_click(cars.bentley)
    home_cars_page.model_dropdown_two_click(cars.bentley_continental_gt)
    home_cars_page.generation_dropdown_two_click(cars.bentley_continental_gt_restyling)
    home_cars_page.filter_search_button_click('href', CAW.audi_bentley)
    home_cars_page.delete_filter_car()
    home_cars_page.search_button_active_filter_click()
    assert home_cars_page.car_model(CAW.bentley) == 'Bentley Continental GT II · Рестайлинг'


#Тесты: Кузов автомобиля
#Тест кузов купе
def test_body_coupe(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click(cars.mercedes)
    home_cars_page.filter_search_button_click('href', CAW.mercedes_benz)
    home_cars_page.dropdown_body(cars.coupe)
    home_cars_page.search_button_active_filter_click()
    sleep(2)
    assert home_cars_page.check_params(CAW.coupe) == 'купе'


#Тест кузов купе
def test_body_(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click(cars.mercedes)
    home_cars_page.filter_search_button_click('href', CAW.mercedes_benz)
    home_cars_page.dropdown_body(cars.coupe)
    home_cars_page.search_button_active_filter_click()
    sleep(2)
    assert home_cars_page.check_params(CAW.coupe) == 'купе'


#Тесты сортировки
#Тест: Минимальная цена
def test_check_min_price(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.car_button_click(cars.dodge)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_min_click()
    assert home_cars_page.price_usd(CAW.min_price) == '≈ 600 $'


#Тест: Максимальная цена
def test_check_max_price(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click(cars.bmw)
    home_cars_page.filter_search_button_click('href', CAW.bmw)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_max_click()
    assert home_cars_page.price_usd(CAW.max_price) == '≈ 276 595 $'


#Тест: Минимальнаый пробег
def test_check_min_mileage(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.filter_search_button_click('href', CAW.all_brand)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_min_mileage_click()
    assert home_cars_page.mileage_car(CAW.min_mileage) == '1 км'


#Тест: Новые по году выпуска
def test_check_new_cars(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.filter_search_button_click('href', CAW.all_brand)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_new_click()
    assert home_cars_page.year_of_manufacture(CAW.year_new) == '2023 г.'


#Тест: Старые по году выпуска
def test_check_old_cars(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.filter_search_button_click('href', CAW.all_brand)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_old_click()
    assert home_cars_page.year_of_manufacture(CAW.year_old) == '1933 г.'


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


