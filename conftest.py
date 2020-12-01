import pytest
import time
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")

    browser = webdriver.Chrome()
    link = f"http://selenium1py.pythonanywhere.com/{browser_lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    yield browser

    print("\nquit browser..")
    browser.quit()