from selenium import webdriver
import BaseClass


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver


class LoginPage(BaseClass):
    def __int__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def loadPage(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.sendkeys("user-name", 'standard_user')
        self.sendkeys("password", 'secret_sauce')
        self.driver.implicitly_wait(10)
        self.clicking('login-button')

login = LoginPage(Driver().get_driver())
login.loadPage()
