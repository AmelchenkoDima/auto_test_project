from selenium.webdriver.common.by import By

#Марка автомобиля из верхнего списка
dodge = (By.XPATH, '//*[@title="Dodge"]')
lexus = (By.XPATH, '//*[@title="Lexus"]')
toyota = (By.XPATH, '//*[@title="Toyota"]')
toyota_gt = (By.XPATH, '//*[@title="GT 86"]')

#Марка автомобиля из выпадающего списка
audi = (By.XPATH, '//*[@data-item-label="Audi"]')
alfa_romeo = (By.XPATH, '//*[@data-item-label="Alfa Romeo"]')
bentley = (By.XPATH, '//*[@id="p-6-1-2-brand"]/div/div/ul/li[7]/button')
bmw = (By.XPATH, '//*[@data-item-label="BMW"]')
mercedes = (By.XPATH, '//*[@data-item-label="Mercedes-Benz"]')

#Модель автомтобиля
audi_80 = (By.XPATH, '//*[@data-item-label="80"]')
bentley_continental_gt = (By.XPATH, '//*[@data-item-label="Continental GT"]')

#Поколение автомобиля
audi_80_b4 = (By.XPATH, '//*[@id="p-6-0-4-generation"]/div/div/div/div/div[4]/label/span[2]')
bentley_continental_gt_restyling = (
    By.XPATH,
    '//*[@id="p-6-1-4-generation"]/div/div/div/div/div[3]/label/span[2]'
)

#Кузов
coupe = (By.XPATH, '//*[@id="p-14-body_type"]/div/div/ul/li[4]/label/span')

#Год автомобиля
year_1998 = (By.XPATH, '//*[@id="p-7-year"]/div/div[1]/ul/li[27]/button')
