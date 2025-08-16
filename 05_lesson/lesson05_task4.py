from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/login")
search_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
search_input.send_keys("tomsmith")
search_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
search_input.send_keys("SuperSecretPassword!")
sleep(10)
button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
button_login.click()
