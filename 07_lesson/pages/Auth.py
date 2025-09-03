from selenium.webdriver.common.by import By


class Auth:
    def __init__(self, driver):
        self.driver = driver

    def input_login(self):
        login = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        login.send_keys("standard_user")

    def input_password(self):
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")

    def submit(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
        button.click()
