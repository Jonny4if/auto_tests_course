from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 15 секунд, пока цена не станет 100
try: 
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )
    button = browser.find_element_by_id("book") 
    button.click() 

    # считаем X
    x_element = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "input_value"))
    )
    x = x_element.text
    y = (math.log(abs(12*math.sin(int(x)))))

    # заполняем и отправляем ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла