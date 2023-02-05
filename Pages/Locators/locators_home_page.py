from selenium.webdriver.common.by import By

cookies = (
        By.XPATH,
        '//button[@class="button button--primary button--large button--block button button--primary"]'
    )
#
lexus_button = (By.XPATH, '//*[@class="catalog__list"]/ul[3]/li[3]/a')
toyota_button = (By.XPATH, '//*[@class="catalog__list"]/ul[20]/li[4]/a')
toyota_gt_button = (By.XPATH, '//*[@class="catalog catalog--rich"]/div/ul[9]/li[2]/a')
dodge_button = (By.XPATH, '//*[@class="catalog__list"]/ul[1]/li[2]/a')

car_header = (By.CLASS_NAME, 'heading__text')

dropdown_brands = (By.XPATH, '//*[@id="p-6-0-2-brand"]/div/div/button')

dropdown_alfa_romeo = (By.XPATH, '//*[@class="dropdown__box"]/ul/li[5]/button')
dropdown_bmw = (By.XPATH, '//*[@class="dropdown__box"]/ul/li[8]/button')

all_brands_button = (By.XPATH, '//*[@class="catalog catalog--rich"]/p/button')
filter_search_button = (By.XPATH, '//*[@class="filter__wrap"]/div/div[2]/a')

dropdown_sort = (By.XPATH,
                 '//*[@id="__next"]/div[2]/main/div/div/div[1]/div[5]/div[3]/div/div[1]/div/div/div/div/button/span')
#//*[@id="__next"]/div[2]/main/div/div/div[1]/div[5]/div[3]/div/div[1]/div/div/div/div/button/span
#//button[@class="dropdown__control dropdown__control--active dropdown-link"]
dropdown_sort_min = (
    By.XPATH,
    '//*[@id="__next"]/div[2]/main/div/div/div[1]/div[5]/div[3]/div/div[1]/div/div/div/div/ul/li[2]/button'
)
#//*[@id="__next"]/div[2]/main/div/div/div[1]/div[5]/div[3]/div/div[1]/div/div/div/div/ul/li[2]/button
#//*[@data-item-label="дешёвые"]
dropdown_sort_max = (By.XPATH, '//*[@class="listing__sort"]/div/div/div/ul/li[3]/button')

price_usd = (By.CLASS_NAME, 'listing-item__priceusd')


scroll_all_brands = '400'

#регистрация
login_button = (By.XPATH, '//*[@class="header"]/div/nav/ul[2]/li[1]/a')
register_button = (By.XPATH, '//*[@class="drawer__view"]/div[1]/div[2]/button')
register_mail_button = (By.XPATH, '//*[@class="drawer__view"]/div[2]/div[1]/div/div[2]/div[1]/button[2]')

name_field = (By.ID, 'name')
mail_field = (By.ID, 'regEmail')
password_fild = (By.ID, 'regPassword')

checkbox_personal_information = (
    By.CLASS_NAME, 'checkbox__input')
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

