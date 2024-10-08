import allure

from burgers_api import BurgersApi
from data import ExpectedAnswers, Body
from helpers import Helpers


class TestCreateOrder:

    @allure.title('Тестируем создание нового заказа с авторизацией, с ингредиентами')
    @allure.description('Запрос должен вернуть {"success": true} и код 200')
    def test_create_order_with_auth_with_ingredients(self, new_user):
        token = new_user.json()['accessToken']
        body = Helpers.mod_create_order_body()
        create_order_response = BurgersApi.create_order(body, token)

        assert create_order_response.status_code == 200 and create_order_response.json()['success'] is True

    @allure.title('Тестируем создание нового заказа без авторизации, с ингредиентами')
    @allure.description('Запрос должен вернуть {"success": true} и код 200')
    def test_create_order_without_auth_with_ingredients(self):
        body = Helpers.mod_create_order_body()
        create_order_response = BurgersApi.create_order(body, token=None)

        assert create_order_response.status_code == 200 and create_order_response.json()['success'] is True

    @allure.title('Тестируем создание нового заказа с авторизацией, без ингредиентов')
    @allure.description('Запрос должен вернуть {"success": false} и код 400')
    def test_create_order_with_auth_without_ingredients(self, new_user):
        token = new_user.json()['accessToken']
        body = []
        create_order_response = BurgersApi.create_order(body, token)
        expected_message = ExpectedAnswers.ORDER_WITHOUT_INGREDIENTS

        assert create_order_response.status_code == 400 and create_order_response.json()['success'] is False \
               and create_order_response.json()['message'] == expected_message

    @allure.title('Тестируем создание нового заказа без авторизации, без ингредиентов')
    @allure.description('Запрос должен вернуть {"success": false} и код 400')
    def test_create_order_without_auth_without_ingredients(self):
        body = []
        create_order_response = BurgersApi.create_order(body, token=None)
        expected_message = ExpectedAnswers.ORDER_WITHOUT_INGREDIENTS

        assert create_order_response.status_code == 400 and create_order_response.json()['success'] is False \
               and create_order_response.json()['message'] == expected_message

    @allure.title('Тестируем создание нового заказа с авторизацией, с невалидным хэшем ингредиента')
    @allure.description('Запрос должен вернуть код 500')
    def test_create_order_with_auth_invalid_hash(self, new_user):
        token = new_user.json()['accessToken']
        body = Body.CREATE_ORDER_BODY_INVALID
        create_order_response = BurgersApi.create_order(body, token)

        assert create_order_response.status_code == 500

    @allure.title('Тестируем создание нового заказа без авторизации, с невалидным хэшем ингредиента')
    @allure.description('Запрос должен вернуть код 500')
    def test_create_order_without_auth_invalid_hash(self):
        body = Body.CREATE_ORDER_BODY_INVALID
        create_order_response = BurgersApi.create_order(body, token=None)

        assert create_order_response.status_code == 500
