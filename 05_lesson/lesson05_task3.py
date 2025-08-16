from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/inputs")
search_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_input.send_keys("Sky")
sleep(10)
search_input.clear()
search_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
sleep(10)
search_input.send_keys("Pro")
sleep(10)
driver.quit()
