import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

input_value = browser.find_element(By.ID, "input_value").text
result = calc(input_value)

browser.execute_script("window.scrollBy(0, 100);")

answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
answer_input.send_keys(result)

robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
robot_checkbox.click()

robots_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
robots_rule_radio.click()

submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

time.sleep(20)
browser.quit()