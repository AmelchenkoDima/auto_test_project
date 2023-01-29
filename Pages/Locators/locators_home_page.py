from selenium.webdriver.common.by import By


all_brands_button = (By.XPATH, '//*[@class="catalog catalog--rich"]/p/button')
lexus_button = (By.XPATH, '//*[@class="catalog__list"]/ul[3]/li[3]/a')
car_header = (By.CLASS_NAME, 'heading__text')
toyota_button = (By.XPATH, '//*[@class="catalog__list"]/ul[20]/li[4]/a')
toyota_gt_button = (By.XPATH, '//*[@class="catalog catalog--rich"]/div/ul[9]/li[2]/a')
scroll_all_brands = '200'
dropdown_brands = (By.XPATH, '//*[@id="p-6-0-2-brand"]/div/div/button')
dropdown_alfa_romeo = (By.XPATH, '//*[@class="dropdown__box"]/ul/li[5]/button')
filter_search_button = (By.XPATH, '//*[@class="filter__wrap"]/div/div[2]/a')
