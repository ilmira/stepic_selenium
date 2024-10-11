from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox.check-input")
    input2.click()
    
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule.check-input")
    input3.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()