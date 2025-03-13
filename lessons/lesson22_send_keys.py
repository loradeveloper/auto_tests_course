import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/file_input.html'
browser.get(link)

first_name = browser.find_element(By. CSS_SELECTOR, "input[name='firstname']")
first_name.send_keys('Alex')

last_name = browser.find_element(By. CSS_SELECTOR, "input[name='lastname']")
last_name.send_keys('Alexandrovich')

email = browser.find_element(By. CSS_SELECTOR, "input[name='email']")
email.send_keys('myemail@gmail.com')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'temp files/empty.txt')           # добавляем к этому пути имя файла

button_send_file = browser.find_element(By.CSS_SELECTOR, "#file")
button_send_file.send_keys(file_path)

submit_button = browser.find_element(By. CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(20)
browser.quit()
