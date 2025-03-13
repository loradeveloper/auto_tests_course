import time
import math
from selenium import webdriver

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/get_attribute.html")

chest = driver.find_element(By.CSS_SELECTOR, "#treasure")
x = chest.get_attribute("valuex")
y = calc(x)

answer_input = driver.find_element(By.CSS_SELECTOR, "#answer")
answer_input.send_keys(y)

robot_checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
robot_checkbox.click()

robots_rule_radio = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
robots_rule_radio.click()

submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

time.sleep(10)
driver.quit()
