from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Александр")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Кормщиков")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Тюмень")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Россия")
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла