from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def find(self, args):
        return self.driver.find_element(*args)

    def finds(self, args):
        return self.driver.find_elements(*args)

    def select(self, args):
        return self.Select(self.driver.find_element(*args))



# def scroll(self, *args):
   #     return self.driver.execute_script(f"window.scrollTo({args}, document.body.scrollHeight);")
