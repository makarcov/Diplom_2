import allure

from burgers_api import BurgersApi
from data import ExpectedAnswers
from helpers import Helpers


class TestUserOrderList:

    @allure.title('Тестируем получение заказов конкретного пользователя с авторизацией')
    @allure.description('Запрос должен вернуть {"success": true} и код 200')
    def test_user_order_list_with_auth(self, new_user):
        token = new_user.json()['accessToken']
        body = Helpers.mod_create_order_body()
        create_order_response = BurgersApi.create_order(body, token)
        order_number = create_order_response.json()['order']['number']
        get_user_order_list_response = BurgersApi.get_user_order_list(token)

        assert get_user_order_list_response.status_code == 200 and get_user_order_list_response.json()['success'] is True \
               and get_user_order_list_response.json()['orders'][0]['number'] == order_number

    @allure.title('Тестируем получение заказов конкретного пользователя без авторизации')
    @allure.description('Запрос должен вернуть {"success": false} и код 401')
    def test_user_order_list_without_auth(self, new_user):
        token = new_user.json()['accessToken']
        body = Helpers.mod_create_order_body()
        BurgersApi.create_order(body, token)
        get_user_order_list_response = BurgersApi.get_user_order_list(token=None)
        expected_answer = ExpectedAnswers.GET_USER_ORDER_LIST_WITHOUT_AUTH

        assert get_user_order_list_response.status_code == 401 and get_user_order_list_response.json()['success'] is False \
               and get_user_order_list_response.json()['message'] == expected_answer