from __future__ import annotations

import allure

from locators.common_locators import CommonLocators
from pages.base_page import BasePage
from urls import BASE_URL


class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open_main(self) -> None:
        self.open(BASE_URL)

    @allure.step('Перейти к созданию рецепта')
    def click_create_recipe(self) -> None:
        self.click(CommonLocators.HEADER_CREATE_RECIPE_BUTTON)

    @allure.step('Проверить отображение кнопки выхода')
    def logout_button_visible(self) -> bool:
        return self.is_visible(CommonLocators.HEADER_LOGOUT_BUTTON)

    @allure.step('Проверить отображение созданного рецепта {recipe_name}')
    def recipe_title_visible(self, recipe_name: str) -> bool:
        return self.is_visible(CommonLocators.recipe_title(recipe_name))
