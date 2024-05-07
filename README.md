# Diplom_2
=======
# Тестирование API сервиса Stellar Burgers

## Описание тестов

- **tests/test_create_order.py** - Тестовый набор для тестирования "Создание заказа"
- **tests/test_create_user.py** - Тестовый набор для тестирования "Создание пользователя"
- **tests/test_edit_user.py** - Тестовый набор для тестирования "Редактирования пользователя"
- **tests/test_get_order_list.py** - Тестовый набор для тестирования "Получения заказов"
- **tests/test_login_user.py** - Тестовый набор для тестирования "Авторизации пользователя"

- **utils/order_utils.py** - Вспомогательные методы для работы с заказами
- **utils/user_utils.py** - Вспомогательные методы для работы с пользователями

- **config.py** - адреса endpoints
- **conftest.py** - содержит фикстуры
- **data.py** - содержит данные для выполнения тестов
- **helpers.py** - содержит вспомогательные методы
- **README.md** - содержит информацию о проекте
- **requirements** - список зависимостей проекта
- **allure_results** - директория с отчетом о тестировании

## Установка зависимостей
```
pip3 install -r requirements.txt
```

## Запуск тестов
```sh
 python -m pytest 
```
## Запуск тестов и генерация Allure-отчёта
```sh
 python -m pytest tests.py --alluredir=allure_results
```
## Отображение отчёта в формате веб-страницы
```sh
 allure serve allure_results
```
