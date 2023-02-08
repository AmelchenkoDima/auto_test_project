from selenium.webdriver.common.by import By

cookies = (
        By.XPATH,
        '//button[@class="button button--primary button--large button--block button button--primary"]'
    )
scroll_all_brands = '400'
#
lexus_button = (By.XPATH, '//*[@class="catalog__list"]/ul[3]/li[3]/a')
toyota_button = (By.XPATH, '//*[@class="catalog__list"]/ul[20]/li[4]/a')
toyota_gt_button = (By.XPATH, '//*[@title="GT 86"')
dodge_button = (By.XPATH, '//*[@class="catalog__list"]/ul[1]/li[2]/a')

car_header = (By.CLASS_NAME, 'heading__text')

car_model = (By.XPATH, '//*[@class="listing__container"]/div[3]/div/div[1]/div/div[2]/h3/a/span')

dropdown_brands = (By.XPATH, '//*[@id="p-6-0-2-brand"]/div/div/button')
dropdown_model = (By.XPATH, '//*[@id="p-6-0-3-model"]/div/div/button')
dropdown_generation = (By.XPATH, '//*[@id="p-6-0-4-generation"]/div/div/button')

dropdown_two_brands = (By.XPATH, '//*[@id="p-6-1-2-brand"]/div/div/button')
dropdown_tow_model = (By.XPATH, '//*[@id="p-6-1-3-model"]/div/div/button')
dropdown_tow_generation = (By.XPATH, '//*[@id="p-6-1-4-generation"]/div/div/button')

dropdown_bentley = (By.XPATH, '//*[@id="p-6-1-2-brand"]/div/div/ul/li[7]/button')
dropdown_bentley_continental_gt = (By.XPATH, '//*[@data-item-label="Continental GT"]')
dropdown_bentley_continental_gt_restyling = (
    By.XPATH,
    '//*[@id="p-6-1-4-generation"]/div/div/div/div/div[3]/label/span[2]'
)
dropdown_audi = (By.XPATH, '//*[@class="dropdown__box"]/ul/li[6]/button')
dropdown_audi_80 = (By.XPATH, '//*[@data-item-label="80"]')
dropdown_audi_80_b4 = (By.XPATH, '//*[@id="p-6-0-4-generation"]/div/div/div/div/div[4]/label/span[2]')
dropdown_alfa_romeo = (By.XPATH, '//*[@class="dropdown__box"]/ul/li[5]/button')
dropdown_bmw = (By.XPATH, '//*[@class="dropdown__box"]/ul/li[8]/button')

all_brands_button = (By.XPATH, '//*[@class="catalog catalog--rich"]/p/button')
filter_search_button = (By.XPATH, '//*[@class="filter__wrap"]/div/div[2]/a')
search_button_active_filter = (By.XPATH, #'//*[@class="filter__show-result"]/button/span')
'//*[@class="filter filter--advert_type-cars"]/div[3]/div/div[3]/div[2]/div[2]/button/span')
dropdown_year_of_manufacture = (By.XPATH, '//*[@id="p-7-year"]/div/div[1]/button/span/span[2]')

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

price_usd = (By.CLASS_NAME, 'listing-item__priceusd')
year_of_manufacture = (By.XPATH, '//*[@class="listing-item__params"]/div[1]')
mileage = (By.XPATH, '//*[@class="listing-item__params"]/div[3]/span')


#Регистрация
login_button = (By.XPATH, '//*[@class="header"]/div/nav/ul[2]/li[1]/a')
register_button = (By.XPATH, '//*[@class="drawer__view"]/div[1]/div[2]/button')
register_mail_button = (By.XPATH, '//*[@class="drawer__view"]/div[2]/div[1]/div/div[2]/div[1]/button[2]')

name_field = (By.ID, 'name')
mail_field = (By.ID, 'regEmail')
password_fild = (By.ID, 'regPassword')

checkbox_personal_information = (
    By.XPATH, '//*[@for="phoneUserEulaAccepted"]'
    #'//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/form/fieldset/div[4]/label/span'
)
register_oneself_button = (
    By.XPATH,
    '//*[@class="drawer__view"]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/form/fieldset/div[5]/button/span'
)

name_error_message = (By.XPATH, '//*[@id="name"]/div')
mail_error_message = (By.XPATH, '//*[@id="regEmail"]/div')
password_error_message = (By.XPATH, '//*[@id="regPassword"]/div')

personal_information = (
    By.XPATH,
    '//*[@class="drawer__slide-body"]/div/div[2]/div[2]/div/div[2]/form/fieldset/div[4]/label/input'
)

