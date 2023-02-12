from selenium.webdriver.common.by import By

cookies = (
        By.XPATH,
        '//button[@class="button button--primary button--large button--block button button--primary"]'
    )
scroll_all_brands = '400'

#
car_header = (By.CLASS_NAME, 'heading__text')
car_model = (By.XPATH, '//*[@class="listing__container"]/div[3]/div/div[1]/div/div[2]/h3/a/span')
price_usd = (By.CLASS_NAME, 'listing-item__priceusd')
year_of_manufacture = (By.XPATH, '//*[@class="listing-item__params"]/div[1]')
car_params = (By.XPATH, '//*[@class="listing-item__params"]/div[2]')
mileage = (By.XPATH, '//*[@class="listing-item__params"]/div[3]/span')

#Выпадающие списки
dropdown_brands = (By.XPATH, '//*[@id="p-6-0-2-brand"]/div/div/button')
dropdown_model = (By.XPATH, '//*[@id="p-6-0-3-model"]/div/div/button')
dropdown_generation = (By.XPATH, '//*[@id="p-6-0-4-generation"]/div/div/button')

dropdown_two_brands = (By.XPATH, '//*[@id="p-6-1-2-brand"]/div/div/button')
dropdown_tow_model = (By.XPATH, '//*[@id="p-6-1-3-model"]/div/div/button')
dropdown_tow_generation = (By.XPATH, '//*[@id="p-6-1-4-generation"]/div/div/button')

dropdown_body = (By.XPATH, '//*[@id="p-14-body_type"]/div/div/button')
dropdown_engine_type = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/button')

dropdown_from_year = (By.XPATH, '//*[@title="Год от"]')
dropdown_until_year = (By.XPATH, '//*[@title="до"]')

#Кнопки поиска
all_brands_button = (By.XPATH, '//*[@class="catalog catalog--rich"]/p/button')
filter_search_button = (By.XPATH, '//*[@class="filter__wrap"]/div/div[2]/a')
search_button_active_filter = (
    By.XPATH,
    '//*[@class="filter filter--advert_type-cars"]/div[3]/div/div[3]/div[2]/div[2]/button/span'
)

#Кнопки
add_filter_button = (By.XPATH, '//*[@class="filter"]/div[2]/div/div[1]/button/span')
delete_filter_button = (
    By.XPATH,
    '//*[@class="filter filter--advert_type-cars"]/div[2]/div/div[2]/div[2]/button'
)

#Сортировка
dropdown_sort = (By.XPATH, '//button[@class="dropdown__control dropdown__control--active dropdown-link"]')
dropdown_sort_min = (By.XPATH, '//*[@data-item-label="дешёвые"]')
dropdown_sort_max = (By.XPATH, '//*[@data-item-label="дорогие"]')
dropdown_sort_min_mileage = (By.XPATH, '//*[@data-item-label="с наименьшим пробегом"]')
dropdown_sort_new = (By.XPATH, '//*[@data-item-label="новые по году"]')
dropdown_sort_old = (By.XPATH, '//*[@data-item-label="старые по году"]')

#Регистрация
login_button = (By.XPATH, '//*[@class="header"]/div/nav/ul[2]/li[1]/a')
register_button = (By.XPATH, '//*[@class="drawer__view"]/div[1]/div[2]/button')
register_mail_button = (By.XPATH, '//*[@class="drawer__view"]/div[2]/div[1]/div/div[2]/div[1]/button[2]')

name_field = (By.ID, 'name')
mail_field = (By.ID, 'regEmail')
password_fild = (By.ID, 'regPassword')

checkbox_personal_information = (By.XPATH, '//*[@for="phoneUserEulaAccepted"]')
register_oneself_button = (
    By.XPATH,
    '//*[@class="drawer__view"]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/form/fieldset/div[5]/button/span'
)

name_error_message = (By.XPATH, '//*[@class="auth__form"]/div[1]/div')
mail_error_message = (By.XPATH, '//*[@class="auth__form"]/div[2]/div')
password_error_message = (By.XPATH, '//*[@class="auth__form"]/div[3]/div')

personal_information = (
    By.XPATH,
    '//*[@class="drawer__slide-body"]/div/div[2]/div[2]/div/div[2]/form/fieldset/div[4]/label/input'
)

