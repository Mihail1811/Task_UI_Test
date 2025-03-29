## Установка зависимостей и запуск тестов

```bash
### Клонирование репозитория

git clone https://github.com/your-repo/first_ui_test.git
cd first_ui_test

### Установка зависимостей

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

### Обычный запуск тестов

pytest tests/test_add_customer.py

### Параллельный запуск тестов с отчетом Allure

pytest -n 2 --alluredir=allure-results
allure serve allure-results