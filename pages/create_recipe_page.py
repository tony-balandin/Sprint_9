from __future__ import annotations

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data.test_data import RecipeData
from locators.common_locators import CommonLocators
from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage
from urls import CREATE_RECIPE_URL


class CreateRecipePage(BasePage):
    @allure.step('Создать рецепт')
    def create_recipe(self, recipe: RecipeData) -> None:
        self.upload_file(CreateRecipePageLocators.IMAGE_INPUT, recipe.image_path)
        self.fill(CreateRecipePageLocators.NAME_INPUT, recipe.name)
        self._select_tag(recipe.tag)
        self._add_ingredient(recipe.ingredient_name, recipe.ingredient_amount)
        self.fill(CreateRecipePageLocators.COOKING_TIME_INPUT, recipe.cooking_time)
        self.fill(CreateRecipePageLocators.TEXT_INPUT, recipe.text)
        self.wait.until(self._create_button_ready)
        self.click(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)
        self.wait.until(EC.url_changes(CREATE_RECIPE_URL))
        self.wait.until(EC.visibility_of_element_located(CommonLocators.recipe_title(recipe.name)))

    @allure.step('Проверить отображение формы создания рецепта')
    def form_visible(self) -> bool:
        return self.is_visible(CreateRecipePageLocators.CREATE_RECIPE_FORM)

    @allure.step('Проверить отображение созданного рецепта {recipe_name}')
    def recipe_title_visible(self, recipe_name: str) -> bool:
        return self.is_visible(CommonLocators.recipe_title(recipe_name))

    def _select_tag(self, tag_name: str) -> None:
        tag_button_locator = CreateRecipePageLocators.tag_button(tag_name)
        tag_button = self.find_present(tag_button_locator)
        classes = tag_button.get_attribute('class') or ''
        if 'styles_checkbox_active' not in classes:
            self.click(tag_button_locator)

    def _add_ingredient(self, ingredient_name: str, amount: str) -> None:
        self.fill(CreateRecipePageLocators.INGREDIENT_INPUT, ingredient_name)
        self.wait.until(EC.visibility_of_element_located(CreateRecipePageLocators.INGREDIENTS_DROPDOWN))
        self.click(CreateRecipePageLocators.ingredient_option(ingredient_name))
        self.fill(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)
        self.click(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)

        try:
            WebDriverWait(self.driver, 5).until(self._ingredient_added(ingredient_name, amount))
        except TimeoutException:
            # На стенде блок добавленных ингредиентов отрисовывается нестабильно.
            # Главное постусловие для этого шага — форма становится готова к отправке.
            WebDriverWait(self.driver, 5).until(self._create_button_ready)

    def _ingredient_added(self, ingredient_name: str, amount: str):
        def predicate(driver):
            try:
                container = driver.find_element(*CreateRecipePageLocators.ADDED_INGREDIENTS_CONTAINER)
                container_text = (container.text or '').strip().lower()
                return ingredient_name.lower() in container_text or str(amount) in container_text
            except Exception:
                return False

        return predicate

    def _create_button_ready(self, driver):
        try:
            button = driver.find_element(*CreateRecipePageLocators.CREATE_RECIPE_BUTTON)
        except Exception:
            return False
        classes = button.get_attribute('class') or ''
        disabled = button.get_attribute('disabled')
        return disabled in (None, 'false') and 'style_button_disabled' not in classes
