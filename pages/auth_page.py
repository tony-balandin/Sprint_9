from __future__ import annotations

import allure
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC

from locators.auth_page_locators import AuthPageLocators
from locators.common_locators import CommonLocators
from pages.base_page import BasePage
from urls import RECIPES_URL, SIGNIN_URL


class AuthPage(BasePage):
    @allure.step('Открыть страницу авторизации')
    def open_login_page(self) -> None:
        self.open(SIGNIN_URL)

    @allure.step('Авторизоваться пользователем')
    def login(self, email: str, password: str, username: str | None = None) -> None:
        attempts = [email]
        if username and username != email:
            attempts.append(username)

        last_error: Exception | None = None
        for identifier in attempts:
            self._submit_credentials(identifier, password)
            try:
                self.wait_for_url_to_be(RECIPES_URL)
                self.wait.until(EC.visibility_of_element_located(CommonLocators.HEADER_LOGOUT_BUTTON))
                return
            except (TimeoutException, UnexpectedAlertPresentException) as error:
                last_error = error
                self._accept_alert_if_present()
                self.open_login_page()

        if last_error is not None:
            raise last_error
        raise AssertionError('Не удалось выполнить авторизацию')

    def _submit_credentials(self, identifier: str, password: str) -> None:
        self.fill(AuthPageLocators.EMAIL_INPUT, identifier)
        self.fill(AuthPageLocators.PASSWORD_INPUT, password)
        self.click(AuthPageLocators.LOGIN_BUTTON)

    def _accept_alert_if_present(self) -> None:
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

    @allure.step('Проверить отображение формы авторизации')
    def login_form_visible(self) -> bool:
        return self.is_visible(AuthPageLocators.LOGIN_FORM)
