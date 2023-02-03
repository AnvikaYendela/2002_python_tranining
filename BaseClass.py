

from selenium.webdriver.common.by import By


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def clicking(self, element):
        self.driver.find_element(By.XPATH, value=element)

    def sendkeys(self, element, input_text):
        self.driver.find_element(By.ID, value=element).send_keys(input_text)
