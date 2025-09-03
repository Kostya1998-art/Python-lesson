from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def push_button(self):
        check = self.driver.find_element(By.ID, "checkout")
        check.click()
