from __future__ import annotations

import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data.test_data import build_unique_user
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage



def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture
def driver(request: pytest.FixtureRequest):
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    remote_url = os.getenv('SELENOID_URL')
    if remote_url:
        options.set_capability('browserName', 'chrome')
        options.set_capability('selenoid:options', {'enableVNC': True, 'enableVideo': False})
        browser = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        options.add_argument('--headless=new')
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def registered_user(registration_page):
    user = build_unique_user()
    registration_page.open_registration_page()
    registration_page.register(user)
    return user


@pytest.fixture
def authorized(driver, registered_user):
    auth = AuthPage(driver)
    auth.open_login_page()
    auth.login(registered_user.email, registered_user.password, registered_user.username)
    return registered_user


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed and 'driver' in item.fixturenames:
        browser = item.funcargs['driver']
        allure.attach(
            browser.get_screenshot_as_png(),
            name='failure-screenshot',
            attachment_type=allure.attachment_type.PNG,
        )
