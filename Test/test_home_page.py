from Pages.home_page import HomePage
from time import sleep


#Тест: 1 авто из закрытого списка
def test_open_car_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.lexus_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Lexus (Лексус) в Беларуси'


#Тест: 1 авто из раскрытого списка
def test_open_car_expanded_list(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.click_all_brands_button()
    home_cars_page.toyota_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Toyota (Тойота) в Беларуси'


#Тест: Молель авто из списка
def test_open_car_toyota_gt(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
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
    home_cars_page.brands_dropdown_click()
    home_cars_page.dropdown_alfa_romeo_click()
    home_cars_page.filter_search_button_click()
    assert home_cars_page.car_header() == 'Продажа автомобилей Alfa Romeo (Альфа Ромео) в Беларуси'


#Тест: Мин цена
def test_check_minimum_price(driver):
    home_cars_page = HomePage(driver)
    home_cars_page.open()
    home_cars_page.dodge_button_click()
    sleep(2)
    home_cars_page.scroll()
    home_cars_page.sort_button_min_click()

    sleep(5)
    assert home_cars_page.price_usd() == '600'
    '''не находит путь к списку сортировки'''

#Тест: Макс цена

