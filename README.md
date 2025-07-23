# Effective Mobile Tests

## Описание

Этот проект содержит автоматизированные тесты для главной страницы сайта effective-mobile.ru.  Используется Python, Playwright, pytest и Allure.

## Установка

1.  Установите Python 3.10.
2.  Клонируйте репозиторий: `git clone <your_repository_url>`
3.  Перейдите в директорию проекта: `cd effective_mobile_tests`
4.  Создайте виртуальное окружение (рекомендуется): `python -m venv venv`
5.  Активируйте виртуальное окружение:
    *   Linux/macOS: `source venv/bin/activate`
    *   Windows: `venv\Scripts\activate`
6.  Установите зависимости: `pip install -r requirements.txt`

## Запуск тестов

### Локально

1.  Убедитесь, что виртуальное окружение активировано.
2.  Запустите тесты: `pytest tests/`

### С использованием Docker

1.  Установите Docker.
2.  Соберите Docker-образ: `docker build -t effective-mobile-tests .`
3.  Запустите контейнер: `docker run effective-mobile-tests`

## Отчеты Allure

После запуска тестов сгенерируйте отчет Allure:

```bash
allure generate allure-results/ -o allure-report
allure open allure-report

Настройка
Вы можете настроить параметры запуска тестов, такие как URL сайта, через переменные окружения. Создайте файл .env в корне проекта и добавьте переменные:

BASE_URL=https://effective-mobile.ru
Затем используйте библиотеку python-dotenv для загрузки этих переменных в ваш код.

Структура проекта
tests/: Содержит тестовые сценарии.
Dockerfile: Файл для сборки Docker-образа.
requirements.txt: Список зависимостей Python.
README.md: Этот файл.
allure-results/: Папка для результатов Allure (игнорируется в git).
