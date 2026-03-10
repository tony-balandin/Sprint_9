from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOGIN_FORM = (
        By.XPATH,
        "//form[contains(@class,'styles_form') and .//input[@name='email'] and .//input[@name='password']]",
    )
    PAGE_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Войти на сайт']",
    )
    EMAIL_INPUT = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//input[@name='email']",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//input[@name='password']",
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//button[normalize-space()='Войти']",
    )
    CREATE_ACCOUNT_LINK = (
        By.XPATH,
        "//a[@href='/signup' and normalize-space()='Создать аккаунт']",
    )
