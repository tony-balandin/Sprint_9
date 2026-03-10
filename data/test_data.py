from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DEFAULT_PASSWORD = 'TestPassword123'
DEFAULT_INGREDIENT = 'лук репчатый'
DEFAULT_INGREDIENT_AMOUNT = '100'
DEFAULT_COOKING_TIME = '15'
DEFAULT_TAG = 'Завтрак'
IMAGE_PATH = Path(__file__).resolve().parent.parent / 'resources' / 'test_image.jpg'


@dataclass(frozen=True)
class UserData:
    email: str
    username: str
    first_name: str
    last_name: str
    password: str


@dataclass(frozen=True)
class RecipeData:
    name: str
    text: str
    ingredient_name: str
    ingredient_amount: str
    cooking_time: str
    image_path: Path
    tag: str = DEFAULT_TAG


def build_unique_user(prefix: str = 'aqa') -> UserData:
    stamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    suffix = stamp[-8:]
    return UserData(
        email=f'{prefix}_{suffix}@ya.ru',
        username=f'{prefix}_{suffix}',
        first_name=f'Anton{suffix[-4:]}',
        last_name='Praktikum',
        password=DEFAULT_PASSWORD,
    )


def build_recipe_data() -> RecipeData:
    stamp = datetime.now().strftime('%H%M%S%f')
    return RecipeData(
        name=f'Автотестовый рецепт {stamp[-6:]}',
        text='Описание рецепта, созданного Selenium-автотестом.',
        ingredient_name=DEFAULT_INGREDIENT,
        ingredient_amount=DEFAULT_INGREDIENT_AMOUNT,
        cooking_time=DEFAULT_COOKING_TIME,
        image_path=IMAGE_PATH,
    )
