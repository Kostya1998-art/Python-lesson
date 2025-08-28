from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    waiter = WebDriverWait(driver, 20)
    waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, """
                                                 "button.btn.
                                                 btn-outline-primary.mt-3")))
                                                 """)))

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")
    first_name.click()

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")
    last_name.click()

    address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address_input.send_keys("Ленина, 55-3")
    address_input.click()

    email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email_address.send_keys("test@skypro.com")
    email_address.click()

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")
    phone_number.click()

    city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city_name.send_keys("Москва")
    city_name.click()

    country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country_name.send_keys("Россия")
    country_name.click()

    job_position = driver.find_element(By.CSS_SELECTOR,
                                       "[name='job-position']")
    job_position.send_keys("QA")
    job_position.click()

    company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company_name.send_keys("SkyPro")
    company_name.click()

    submit_button = driver.find_element(By.CSS_SELECTOR,
                                        "button.btn.btn-outline-primary.mt-3")
    submit_button.click()
    zip_code = driver.find_element(By.CSS_SELECTOR,
                                   "[id='zip-code']").value_of_css_property
    ("background-color")

    assert zip_code == "rgba(248, 215, 218, 1)"
    fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job", "company"]

    for field in fields:
        field = driver.find_element(By.CSS_SELECTOR,
                                    "div#first-name.alert.py-2.alert-success")
        field.value_of_css_property("background-color")
    assert field == "rgba(209, 231, 221, 1)"
    driver.quit()
