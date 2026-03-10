from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    CREATE_RECIPE_FORM = (
        By.XPATH,
        "//form[.//input[@type='file'] and .//button[normalize-space()='Создать рецепт']]",
    )
    PAGE_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Создание рецепта']",
    )
    NAME_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Название рецепта']]//input",
    )
    TEXT_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Описание рецепта']]//textarea",
    )
    IMAGE_INPUT = (
        By.XPATH,
        "//input[@type='file']",
    )
    INGREDIENT_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Ингредиенты']]//input",
    )
    INGREDIENT_AMOUNT_INPUT = (
        By.XPATH,
        "//input[contains(@class,'styles_ingredientsAmountValue')]",
    )
    ADD_INGREDIENT_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'styles_ingredientAdd') and normalize-space()='Добавить ингредиент']",
    )
    ADDED_INGREDIENTS_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'styles_ingredientsAdded')]",
    )
    COOKING_TIME_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Время приготовления']]//input",
    )
    CREATE_RECIPE_BUTTON = (
        By.XPATH,
        "//form//button[normalize-space()='Создать рецепт']",
    )
    INGREDIENTS_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class,'styles_container__3ukwm')]",
    )

    @staticmethod
    def ingredient_option(option_text: str) -> tuple[str, str]:
        escaped = option_text.replace("'", '"')
        return (
            By.XPATH,
            (
                f"//div[contains(@class,'styles_container__3ukwm')]/div[normalize-space()='{escaped}']"
            ),
        )

    @staticmethod
    def tag_button(tag_name: str) -> tuple[str, str]:
        escaped = tag_name.replace("'", '"')
        return (
            By.XPATH,
            (
                f"//*[normalize-space()='{escaped}']"
                "/parent::*[self::div or self::span][1]"
                "/preceding-sibling::button[1]"
                " | "
                f"//*[normalize-space()='{escaped}']/ancestor::div[1]//button[1]"
            ),
        )
