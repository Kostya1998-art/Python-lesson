from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    driver.get("https://www.saucedemo.com/")

    login = driver.find_element(By.CSS_SELECTOR,
                                "#user-name.input_error.form_input")
    login.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password.input_error.form_input")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.CSS_SELECTOR,
                                 "#login-button.submit-button.btn_action")
    button.click()

    backpack = driver.find_element(By.CSS_SELECTOR, """
                                   "#add-to-cart-sauce-labs-backpack.btn
                                   .btn_primary.btn_small.btn_inventory")
                                   """)
    backpack.click()

    t_shirt = driver.find_element(By.CSS_SELECTOR, """
                                  "#add-to-cart-sauce-labs-bolt-t-shirt.btn
                                  .btn_primary.btn_small.btn_inventory")
                                """)
    t_shirt.click()

    onesie = driver.find_element(By.CSS_SELECTOR, """
                                                #add-to-cart-sauce-labs-onesie.btn
                                                .btn_primary.btn_small.btn_inventory
                                                """)
    onesie.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
    cart.click()

    check = driver.find_element(By.CSS_SELECTOR, """
                                "#checkout.btn
                                .btn_action.btn_medium.checkout_button")
                                """)
    check.click()

    name = driver.find_element(By.CSS_SELECTOR,
                               "#first-name.input_error.form_input")
    name.send_keys("Константин")

    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#last-name.input_error.form_input")
    last_name.send_keys("Беляков")

    postal = driver.find_element(By.CSS_SELECTOR,
                                 "#postal-code.input_error.form_input")
    postal.send_keys("195256")

    next = driver.find_element(By.CSS_SELECTOR, """
                               "#continue.submit-button.btn
                               .btn_primary.cart_button.btn_action")
                               """)
    next.click()

    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label")
    assert total.text == "Total: $58.29"
