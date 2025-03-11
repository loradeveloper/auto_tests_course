import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
)

button = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#book"))
)
button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text

input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
input_answer.send_keys(calc(input_value))

submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(20)
browser.quit()