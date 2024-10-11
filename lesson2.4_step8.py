from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100")):    
        browser.find_element(By.CSS_SELECTOR, "#book.btn-primary").click()
    else: print("Не нашлась цена 100!")
    
    browser.execute_script("window.scrollBy(0, 100);")
    
    x = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap").text
    y = calc(x)
    
    browser.find_element(By.CSS_SELECTOR, "#answer.form-control").send_keys(y)
    
    browser.find_element(By.CSS_SELECTOR, "#solve.btn.btn-primary").click()
    
    alert = browser.switch_to.alert
    print(alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла