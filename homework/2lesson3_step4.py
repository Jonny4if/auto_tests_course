from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
  link = "http://suninjuly.github.io/alert_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # Нажимаем кнопку
  button = browser.find_element_by_css_selector("button.btn")
  button.click()

  # закрываем модальное окно
  confirm = browser.switch_to.alert
  confirm.accept()

  # считаем X и Y
  x_num = browser.find_element_by_id('input_value')
  x = int(x_num.text)
  summa = str(math.log(abs(12*math.sin(x))))
  
  # Заполненяем форму
  input1 = browser.find_element_by_id("answer")
  input1.send_keys(summa)

  # Нажимаем кнопку
  button = browser.find_element_by_css_selector("button.btn")
  button.click()


 

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()

  # не забываем оставить пустую строку в конце файла