from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    n1 = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    n2 = num2.text
    sum_of_nums = int(n1) + int(n2)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum_of_nums)) 
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()