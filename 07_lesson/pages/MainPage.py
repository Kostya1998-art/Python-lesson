from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_goods(self):

        backpack = self.driver.find_element(By.ID,
                                            "add-to-cart-sauce-labs-backpack")
        backpack.click()

        locator = "add-to-cart-sauce-labs-bolt-t-shirt"
        t_shirt = self.driver.find_element(By.ID, locator)
        t_shirt.click()

        onesie = self.driver.find_element(By.ID,
                                          "add-to-cart-sauce-labs-onesie")
        onesie.click()

    def go_to_cart(self):

        cart = self.driver.find_element(By.CSS_SELECTOR,
                                        "a.shopping_cart_link")
        cart.click()
