from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
  link = "http://SunInJuly.github.io/execute_script.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # считаем X и Y
  x_num = browser.find_element_by_id('input_value')
  x = int(x_num.text)
  summa = str(math.log(abs(12*math.sin(x))))
  
  # Заполняем форму
  input1 = browser.find_element_by_id("answer")
  input1.send_keys(summa)

  # Проставляем чекбокс и батон
  option1 = browser.find_element_by_id("robotCheckbox")
  option1.click()
  option2 = browser.find_element_by_id("robotsRule")
  browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
  option2.click()

  # Отправляем заполненную форму
  button = browser.find_element_by_css_selector('button[type="submit"]')
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  button.click()
 

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()

  # не забываем оставить пустую строку в конце файла