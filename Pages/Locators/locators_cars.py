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
fiat = (By.XPATH, '//*[@data-item-label="Fiat"]')
ford = (By.XPATH, '//*[@data-item-label="Ford"]')
mercedes = (By.XPATH, '//*[@data-item-label="Mercedes-Benz"]')
porsche = (By.XPATH, '//*[@data-item-label="Porsche"]')
volkswagen = (By.XPATH, '//*[@data-item-label="Volkswagen"]')

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
minivan = (By.XPATH, '//*[@id="p-14-body_type"]/div/div/ul/li[10]/label/span')
limousine = (By.XPATH, '//*[@id="p-14-body_type"]/div/div/ul/li[6]/label/span')
other = (By.XPATH, '//*[@id="p-14-body_type"]/div/div/ul/li[17]/label/span')

#Год автомобиля
from_year_1998 = (By.XPATH, '//*[@data-item-label="1998"]')
until_year_1998 = (By.XPATH, '//*[@id="p-7-year"]/div/div[2]/ul/li[27]/button')

#Тип двигателя
petrol = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/ul/li[1]/label/span')
petrol_propane_butane = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/ul/li[2]/label/span')
petrol_methane = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/ul/li[3]/label/span')
petrol_hybrid = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/ul/li[4]/label/span')
diesel = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/ul/li[5]/label/span')
diesel_hybrid = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/ul/li[6]/label/span')
electro = (By.XPATH, '//*[@id="p-15-engine_type"]/div/div/ul/li[7]/label/span')
