# Effective Mobile Tests

## Описание

Этот проект содержит автоматизированные тесты для главной страницы сайта effective-mobile.ru.  Используется Python, Playwright, Allure и Docker.

## Предварительные требования

*   Docker
*   Python 3.10 (рекомендуется использовать виртуальное окружение)

## Установка

1.  Клонируйте репозиторий:

    ```bash
    git clone <your_repository_url>
    cd effective_mobile_tests
(Опционально) Создайте и активируйте виртуальное окружение:

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
Установите зависимости:

pip install -r requirements.txt
Запуск тестов
Локально (без Docker):
pytest src/tests/
С использованием Docker:
Соберите Docker-образ:

docker build -t effective-mobile-tests .
Запустите контейнер:

docker run -v $(pwd)/allure-results:/app/allure-results effective-mobile-tests
(Опционально) Для Windows:

docker run -v %cd%/allure-results:/app/allure-results effective-mobile-tests
Отчеты Allure
После запуска тестов с Docker, отчеты Allure будут доступны в папке allure-results. Для просмотра отчета:

Установите Allure:

#  Проверьте, установлен ли Allure:
allure --version

# Если нет, установите (пример для macOS с использованием Homebrew):
brew install allure
Сгенерируйте отчет:

allure generate allure-results -o allure-report
Откройте отчет в браузере:

allure open allure-report
Замечания
Убедитесь, что сайт effective-mobile.ru доступен во время запуска тестов.
При необходимости, настройте параметры Playwright (например, headless режим) в файле conftest.py.
