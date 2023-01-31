from selenium.webdriver.common.by import By

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

dropdown_sort = (By.CLASS_NAME, 'dropdown__box')
dropdown_sort_min = (By.XPATH, '//*[@class="listing__sort"]/div/div/div/ul/li[2]/button')
dropdown_sort_max = (By.XPATH, '//*[@class="listing__sort"]/div/div/div/ul/li[3]/button')

price_usd = (By.CLASS_NAME, 'listing-item__priceusd')


scroll_all_brands = '400'
