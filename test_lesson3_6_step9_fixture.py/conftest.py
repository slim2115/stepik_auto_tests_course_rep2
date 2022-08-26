from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


#pytest_addoption(parser) - это метод, который позволяет запускать тест, который зависит от опции командной строки.
#parser - этот атрибут считывает значения из строки.

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru", help="Choose language: es or fr or 'etc'")

# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")
# request - объект для анализа контекста запрашивающей тестовой функции, класса или модуля.
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    user_language = request.config.getoption("language")  # получаем параметр командной строки language
    #browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {"intl.accept_browsers": browser_name})
        options.add_experimental_option('prefs', {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_browsers", browser_name)
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()