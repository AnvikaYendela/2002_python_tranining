from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium import webdriver


class ProductManagement(ABC):

    @abstractmethod
    def getProductNames(self):
        pass

    @abstractmethod
    def getProductCount(self):
        pass


class HomePage(ProductManagement):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def loadPage(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,"user-name").send_keys('standard_user')

        self.driver.find_element(By.ID,'password').send_keys('secret_sauce')

        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, 'login-button').click()
        self.driver.implicitly_wait(20)

    def getProductNames(self):
       products = self.driver.find_elements(By.CSS_SELECTOR, "div.inventory_item_name")
       for value in products:
           print(value.text)

    def getProductCount(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, "div.inventory_item_name")
        print(len(products))


google = HomePage()
google.loadPage()
google.getProductNames()
google.getProductCount()
