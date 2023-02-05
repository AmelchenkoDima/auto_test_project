from Pages.home_page import HomePage
from Pages.Locators import login_field_arguments as arg
from time import sleep


#Тест: 1 авто из закрытого списка
def test_open_car_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.lexus_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Lexus (Лексус) в Беларуси'


#Тест: 1 авто из раскрытого списка
def test_open_car_expanded_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.click_all_brands_button()
    home_cars_page.toyota_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Toyota (Тойота) в Беларуси'


#Тест: Молель авто из списка
def test_open_car_toyota_gt(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.click_all_brands_button()
    home_cars_page.toyota_button_click()
    home_cars_page.scroll()
    home_cars_page.toyota_gt_button_click()
    sleep(3) #временный слип тк страница не успевает прогрузится
    assert home_cars_page.car_header() == 'Продажа автомобилей Toyota GT 86'


#Тест: 1 авто из выпадающего списка
def test_open_car_dropdown(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click()
    home_cars_page.dropdown_alfa_romeo_click()
    home_cars_page.filter_search_button_click() #урл ожид
    assert home_cars_page.car_header() == 'Продажа автомобилей Alfa Romeo (Альфа Ромео) в Беларуси'


#Тест: Мин цена
def test_check_min_price(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.dodge_button_click()
    #sleep(2)
    #home_cars_page.scroll()
    #sleep(2)
    home_cars_page.sort_button_click()
    home_cars_page.sort_button_min_click()

    #sleep(5)
    assert home_cars_page.price_usd() == '600'
    '''не находит путь к списку сортировки'''


#Тест: Макс цена
def test_check_max_price(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.cookies_window_close()
    home_cars_page.brands_dropdown_click()
    home_cars_page.scroll()
    home_cars_page.dropdown_bmw_click()
    home_cars_page.filter_search_button_click()
    home_cars_page.scroll()
    sleep(3)
    home_cars_page.sort_button_click()
    sleep(3)


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


def test_register_invalid_password_aql(driver):
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


