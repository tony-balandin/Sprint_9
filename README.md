# Foodgram UI tests

Учебный проект по Selenium и pytest для сервиса Foodgram.

## Покрытые сценарии
- создание аккаунта;
- авторизация;
- создание рецепта.

## Структура проекта
- `pages/` — Page Object классы;
- `locators/` — локаторы страниц;
- `tests/` — тесты по функциональностям;
- `data/` — тестовые данные и генераторы;
- `Dockerfile`, `docker-compose.yml` — запуск в контейнерах;
- `.github/workflows/ci.yml` — GitHub Actions.

## Локальный запуск
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests -v
```

## Запуск с Allure
```bash
pytest tests --alluredir=allure-results
allure generate allure-results -o allure-report --clean
```

## Запуск через Docker Compose
```bash
docker compose up -d selenoid
SELENOID_URL=http://localhost:4444/wd/hub pytest tests -v --alluredir=allure-results
```

## Перед сдачей
1. Выполните локальный или CI-прогон без падений.
2. Перегенерируйте `allure-report` после успешного прогона.
3. Замените `screens/pipeline_success.png` реальным скрином успешного GitHub Actions pipeline.
