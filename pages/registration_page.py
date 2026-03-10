from __future__ import annotations

import allure

from data.test_data import UserData
from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage
from urls import SIGNIN_URL, SIGNUP_URL


class RegistrationPage(BasePage):
    @allure.step('Открыть страницу регистрации')
    def open_registration_page(self) -> None:
        self.open(SIGNUP_URL)

    @allure.step('Зарегистрировать нового пользователя')
    def register(self, user: UserData) -> None:
        self.fill(RegistrationPageLocators.FIRST_NAME_INPUT, user.first_name)
        self.fill(RegistrationPageLocators.LAST_NAME_INPUT, user.last_name)
        self.fill(RegistrationPageLocators.USERNAME_INPUT, user.username)
        self.fill(RegistrationPageLocators.EMAIL_INPUT, user.email)
        self.fill(RegistrationPageLocators.PASSWORD_INPUT, user.password)
        self.click(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        self.wait_for_url_contains(SIGNIN_URL)

    @allure.step('Проверить отображение формы регистрации')
    def registration_form_visible(self) -> bool:
        return self.is_visible(RegistrationPageLocators.REGISTRATION_FORM)
