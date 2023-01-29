from Pages.home_page import HomePage
from time import sleep


def test_open_car_lexus(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.lexus_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Lexus (Лексус) в Беларуси'


def test_open_car_toyota(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.click_all_brands_button()
    home_cars_page.toyota_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Toyota (Тойота) в Беларуси'


def test_open_car_toyota_gt(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.click_all_brands_button()
    home_cars_page.toyota_button_click()
    home_cars_page.scroll_all_brands_button()
    home_cars_page.toyota_gt_button_click()
    sleep(3) #временный слип тк страница не успевает прогрузится
    assert home_cars_page.car_header() == 'Продажа автомобилей Toyota GT 86'


def test_open_car_dropdown(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.brands_dropdown_click()
    home_cars_page.dropdown_alfa_romeo_click()
    home_cars_page.filter_search_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Alfa Romeo (Альфа Ромео) в Беларуси'



