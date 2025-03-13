import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# Допустимые значения scope: “function”, “class”, “module”, “session”
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# Фикстура используется автоматически для всех тестов
@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():

    # Для запуска тестов с нужной маркировкой:
    # pytest -s -v -m smoke filename.py
    # Для запуска всех тестов, КРОМЕ smoke:
    # pytest -s -v -m "not smoke" filename.py
    # Можно применять логические операторы
    @pytest.mark.smoke
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    # Только regression для windows 10:
    # pytest -s -v -m "regression and win10" filename.py
    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

    # Такой меткой помечаются тесты, которые ожидаемо упадут при наличии багов
    # Чтобы не влиял на конечный результат, будет skipped
    # skip должен быть последним маркером
    @pytest.mark.skip
    def test_skip(self):
        print("will be skipped anyway")