import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

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

    sleep(100)

finally:
    sleep(30)
    browser.quit()
