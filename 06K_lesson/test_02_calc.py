from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    url = "https://bonigarcia.dev/selenium-webdriver-java/" \
        "slow-calculator.html"
    driver.get(url)
    number = driver.find_element(By.CSS_SELECTOR, "#delay")
    number.clear()
    number.send_keys("45")

    button = driver.find_element(By.CSS_SELECTOR,
                                 "span.btn.btn-outline-primary")
    button.click()

    button_plus = driver.find_element(By.CSS_SELECTOR,
                                      "span.operator.btn.btn-outline-success")
    button_plus.click()

    button_eight = driver.find_element(By.XPATH, "//span[text()='8']")
    button_eight.click()

    button_equal = driver.find_element(By.CSS_SELECTOR,
                                       "span.btn.btn-outline-warning")
    button_equal.click()

    wait = WebDriverWait(driver, 45)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                 "div.screen"), "15"))
    assert driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"
