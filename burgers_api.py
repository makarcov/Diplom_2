import allure
import requests

from data import Url
from endpoints import Endpoint


class BurgersApi:

    @staticmethod
    @allure.step('Создаем нового пользователя')
    def create_user(body):
        create_user_response = requests.post(Url.BASE_URL + Endpoint.CREATE_USER_ENDPOINT, json=body)
        return create_user_response

    @staticmethod
    @allure.step('Удаляем пользователя')
    def delete_user(token):
        delete_user_response = requests.delete(Url.BASE_URL + Endpoint.DELETE_USER_ENDPOINT, headers={
            'Authorization': token
        })
        return delete_user_response

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(body):
        login_user_response = requests.post(Url.BASE_URL + Endpoint.LOGIN_USER_ENDPOINT, json=body)
        return login_user_response

    @staticmethod
    @allure.step('Обновляем информацию пользователя')
    def update_user_info(body, token):
        update_user_response = requests.patch(Url.BASE_URL + Endpoint.UPDATE_USER_INFO_ENDPOINT, json=body, headers={
            'Authorization': token
        })
        return update_user_response

    @staticmethod
    @allure.step('Создаем новый заказ')
    def create_order(body, token):
        create_order_response = requests.post(Url.BASE_URL + Endpoint.CREATE_ORDER_ENDPOINT, json=body, headers={
            'Authorization': token
        })
        return create_order_response

    @staticmethod
    @allure.step('Получаем список ингредиентов')
    def get_ingredients():
        get_ingredients_response = requests.get(Url.BASE_URL + Endpoint.GET_INGREDIENTS_ENDPOINT)
        return get_ingredients_response

    @staticmethod
    @allure.step('Получаем список заказов пользователя')
    def get_user_order_list(token):
        get_user_order_list_response = requests.get(Url.BASE_URL + Endpoint.GET_USER_ORDER_LIST_ENDPOINT, headers={
            'Authorization': token
        })
        return get_user_order_list_response
