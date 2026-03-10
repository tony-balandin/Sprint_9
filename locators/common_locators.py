from selenium.webdriver.common.by import By


class CommonLocators:
    HEADER_LOGIN_BUTTON = (
        By.XPATH,
        "//a[@href='/signin' and normalize-space()='Войти']",
    )
    HEADER_CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//a[@href='/signup' and normalize-space()='Создать аккаунт']",
    )
    HEADER_CREATE_RECIPE_BUTTON = (
        By.XPATH,
        "//a[@href='/recipes/create' and normalize-space()='Создать рецепт']",
    )
    HEADER_LOGOUT_BUTTON = (
        By.XPATH,
        "//a[normalize-space()='Выход']",
    )
    RECIPES_TAB = (
        By.XPATH,
        "//a[@href='/recipes' and normalize-space()='Рецепты']",
    )

    @staticmethod
    def recipe_title(recipe_name: str) -> tuple[str, str]:
        escaped = recipe_name.replace("'", '"')
        return (
            By.XPATH,
            (
                f"//h1[normalize-space()='{escaped}']"
                f" | //a[@href[contains(., '/recipes/')] and normalize-space()='{escaped}']"
            ),
        )
