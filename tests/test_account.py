import allure

from data.test_data import build_unique_user
from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
from urls import SIGNIN_URL


@allure.epic('Foodgram UI')
@allure.feature('Создание аккаунта')
class TestAccountCreation:
    @allure.title('Успешное создание аккаунта переводит на страницу авторизации')
    def test_create_account_redirects_to_login(self, driver):
        registration_page = RegistrationPage(driver)
        auth_page = AuthPage(driver)
        user = build_unique_user()

        registration_page.open_registration_page()
        registration_page.register(user)

        assert auth_page.current_url() == SIGNIN_URL
        assert auth_page.login_form_visible() is True
