import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/redirect_accept.html'
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

browser.switch_to.window(browser.window_handles[1])


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text

input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
input_answer.send_keys(calc(input_value))

submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(20)
browser.quit()