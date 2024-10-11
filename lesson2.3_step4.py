from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
        
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap").text
    y = calc(x)
    
    browser.find_element(By.CSS_SELECTOR, "#answer.form-control").send_keys(y)
    
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла