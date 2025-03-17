import time
import math
import json
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = \
    [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
    ]

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config_stepik.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)

        return config

@pytest.mark.parametrize('link', links)
class TestAuthorization:
    def test_authorization(self, browser, load_config, link):
        try:
            browser.implicitly_wait(10)
            browser.get(link)
            login = load_config['login']
            password = load_config['password']

            login_in_link = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']"))
            )
            login_in_link.click()

            input_email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
            input_email.send_keys(login)

            input_password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
            input_password.send_keys(password)

            login_in_button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
            login_in_button.click()

            # Проверить, было ли отправлено решение. Если да, то решить снова
            solve_again_button = browser.find_elements(By.CSS_SELECTOR, "button[class='again-btn white']")
            if solve_again_button:
                solve_again_button[0].click()
                alert = browser.find_elements(By.CSS_SELECTOR, "div.modal-popup__container button")
                if alert:
                    alert[1].click()

            #input_answer = browser.find_element(By.CSS_SELECTOR, "textarea[class='ember-text-area ember-view textarea string-quiz__textarea']")
            input_answer = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class='ember-text-area ember-view textarea string-quiz__textarea']"))
            )
            input_answer.clear()
            input_answer.send_keys(str(math.log(int(time.time()))))

            # send_button = browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']")
            send_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='submit-submission']"))
            )
            send_button.click()

            is_correct_text = browser.find_elements(By.CSS_SELECTOR, "div[class='smart-hints ember-view lesson__hint']")
            # Если решение неправильное, то записываем текст ошибки в файл
            if is_correct_text:
                text = is_correct_text[0].text
            # Если правильное, то тоже записываем в файл
            else:
                text = browser.find_element(By.CSS_SELECTOR, "p[class='smart-hints__hint']").text
            with open("code_words.txt", "a", encoding="utf-8") as file:
                file.write(f"{link} {text}\n")

        finally:
            time.sleep(1)