from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))

# Перейти на страницу

driver.get("http://uitestingplayground.com/textinput")
# Найти поисковик
search_input = driver.find_element(By.CSS_SELECTOR, "input.form-control")
search_input.send_keys("SkyPro")
# Нажать кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
# Подождать вывода текста
wait = WebDriverWait(driver, 16)
content = wait.until(EC.visibility_of_element_located
                     ((By.CSS_SELECTOR, "button.btn-primary")))
txt = content.text
print(txt)

driver.quit()
