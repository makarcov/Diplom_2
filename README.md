# API тесты

## Тестирование сайтa Stellar Burgers

### Описание файлов и директорий:
#### Файлы

*conftest.py* - файл с настройками (фикстурами)

*burgers_api.py* - файл с методами запросов ручек

*endpoints.py* - файл с ручками

*helpers.py* - файл с вспомогательными функциями

*data.py* - файл с вспомогательной информацией

*requirements.txt* - файл с зависимостями

#### Directory "tests":
*test_create_order.py* - тесты ручки создания заказа

*test_create_user.py* - тесты ручки создания пользователя

*test_login_user.py* - тесты ручки авторизации пользователя

*test_update_user_info.py* - тесты ручки обновления информации пользователя

*test_user_order_list.py* - тесты ручки получения списка заказов пользователя

#### Directory "allure_results":
отчет о тестах

#### **Для запуска тестов**: pytest
#### **Установка зависимостей**: pip install -r requirements.txt`
