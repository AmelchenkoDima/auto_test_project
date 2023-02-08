from selenium.webdriver.common.by import By

#Год автомобиля
year_1998 = (By.XPATH, '//*[@id="p-7-year"]/div/div[1]/ul/li[27]/button')


#Марка автомобиля
bentley = (By.XPATH, '//*[@id="p-6-1-2-brand"]/div/div/ul/li[7]/button')

#Модель автомтобиля
bentley_continental_gt = (By.XPATH, '//*[@data-item-label="Continental GT"]')

#Поколение автомобиля
bentley_continental_gt_restyling = (By.XPATH, '//*[@class="dropdown__cards"]/div[3]/label/span[2]')
