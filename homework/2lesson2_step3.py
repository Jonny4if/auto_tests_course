from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
  link = "http://suninjuly.github.io/selects2.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # считаем X и Y
  x_num = browser.find_element_by_id('num1')
  y_num = browser.find_element_by_id('num2')
  x = int(x_num.text)
  y = int(y_num.text)
  summa = str(x + y)
  
  # Выбираем элемент списка
  select = Select(browser.find_element_by_id("dropdown"))
  select.select_by_value(summa) 

  # Отправляем заполненную форму
  button = browser.find_element_by_css_selector('button[type="submit"]')
  button.click()
 

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()

  # не забываем оставить пустую строку в конце файла