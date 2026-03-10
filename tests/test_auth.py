import allure

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from urls import RECIPES_URL


@allure.epic('Foodgram UI')
@allure.feature('Авторизация')
class TestAuthorization:
    @allure.title('Успешная авторизация переводит на страницу рецептов и показывает кнопку выхода')
    def test_login_redirects_to_recipes_page(self, driver, registered_user):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)

        auth_page.open_login_page()
        auth_page.login(registered_user.email, registered_user.password, registered_user.username)

        assert auth_page.current_url() == RECIPES_URL
        assert main_page.logout_button_visible() is True
