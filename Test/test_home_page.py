from Pages.home_page import HomePage as HP


def test_open_lexus(driver):
    home_page = HP(driver)
    home_page.open()
    home_page.lexus_open()
    assert home_page.lexus_page() == 'Продажа автомобилей Lexus (Лексус) в Беларуси'
# не проходит тк не верная ссылка на лексус (найти новую ссылку)

