from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REGISTRATION_FORM = (
        By.XPATH,
        "//form[contains(@class,'styles_form') and .//input[@name='first_name'] and .//input[@name='last_name'] and .//input[@name='username']]",
    )
    PAGE_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Регистрация']",
    )
    FIRST_NAME_INPUT = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//input[@name='first_name']",
    )
    LAST_NAME_INPUT = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//input[@name='last_name']",
    )
    USERNAME_INPUT = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//input[@name='username']",
    )
    EMAIL_INPUT = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//input[@name='email']",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//input[@name='password']",
    )
    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//form[contains(@class,'styles_form')]//button[normalize-space()='Создать аккаунт']",
    )
