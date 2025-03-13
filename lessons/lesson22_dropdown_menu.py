import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import os

driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/selects1.html")

num1 = int(driver.find_element(By.ID, "num1").text)
num2 = int(driver.find_element(By.ID, "num2").text)
sum = num1 + num2

select = Select(driver.find_element(By.ID, "dropdown"))
time.sleep(3)
select.select_by_value(str(sum))
# select.select_by_visible_text("text")
# select.select_by_index(index)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(20)