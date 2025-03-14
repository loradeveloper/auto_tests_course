import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config_stepik.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config


@pytest.mark.smoke
class TestAuthorization:
    def test_authorization(self, browser, load_config):
        try:
            browser.implicitly_wait(10)
            browser.get(link)
            login = load_config['login']
            password = load_config['password']

            answer = math.log(int(time.time()))

            input_answer = browser.find_element(By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...'")
            input_answer.send_keys(answer)

            send_button = browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']")
            send_button.click()

            # login_in_link = browser.find_element(By.LINK_TEXT, "Войти")
            # login_in_link.click()
            login_in_link = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-tab-name='login']"))
            )
            login_in_link.click()

            input_email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
            input_email.send_keys(login)

            input_password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
            input_password.send_keys(password)

            login_in_button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
            login_in_button.click()
        finally:
            time.sleep(10)