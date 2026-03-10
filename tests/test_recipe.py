import re

import allure

from data.test_data import build_recipe_data
from pages.create_recipe_page import CreateRecipePage
from pages.main_page import MainPage
from urls import CREATE_RECIPE_URL, BASE_URL


@allure.epic('Foodgram UI')
@allure.feature('Создание рецепта')
class TestRecipeCreation:
    @allure.title('Авторизованный пользователь может создать рецепт')
    def test_authorized_user_can_create_recipe(self, driver, authorized):
        main_page = MainPage(driver)
        recipe_page = CreateRecipePage(driver)
        recipe = build_recipe_data()

        main_page.open_main()
        main_page.click_create_recipe()

        assert recipe_page.current_url() == CREATE_RECIPE_URL
        assert recipe_page.form_visible() is True

        recipe_page.create_recipe(recipe)

        assert re.fullmatch(rf'{re.escape(BASE_URL)}/recipes/\d+', recipe_page.current_url()) is not None
        assert recipe_page.recipe_title_visible(recipe.name) is True
