from selenium.webdriver.common.by import By


class Order:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):

        name = self.driver.find_element(By.CSS_SELECTOR,
                                        "#first-name.input_error.form_input")
        name.send_keys("Константин")

        locator = "#last-name.input_error.form_input"
        last_name = self.driver.find_element(By.CSS_SELECTOR, locator)

        last_name.send_keys("Беляков")

        loc = "#postal-code.input_error.form_input"
        postal = self.driver.find_element(By.CSS_SELECTOR, loc)
        postal.send_keys("195256")

        next = self.driver.find_element(By.ID, "continue")
        next.click()

    def check_cost(self):
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         "div.summary_total_label")
        return total
