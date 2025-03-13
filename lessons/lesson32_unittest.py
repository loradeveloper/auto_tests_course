import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_my1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        first_name_input.send_keys("Ivan")

        last_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        last_name_input.send_keys("Ivanov")

        email_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        email_input.send_keys("ivanov@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Welcome text is not successfully")

        time.sleep(2)
        browser.quit()

    def test_my2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        first_name_input.send_keys("Ivan")

        last_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        last_name_input.send_keys("Ivanov")

        email_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        email_input.send_keys("ivanov@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Welcome text is not successfully")

        time.sleep(2)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
