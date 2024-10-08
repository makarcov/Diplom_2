import allure
import pytest

from burgers_api import BurgersApi
from helpers import Helpers


class TestLoginUser:

    @allure.title('Тестируем авторизацию существующего пользователя')
    @allure.description('Запрос должен вернуть в тексте ответа {"success": true} и код 200')
    def test_login_user(self):
        body = Helpers.mod_create_user_body()
        create_response = BurgersApi.create_user(body)
        login_response = BurgersApi.login_user(body)

        assert login_response.status_code == 200 and login_response.json()['success'] is True
        BurgersApi.delete_user(create_response.json()['accessToken'])

    @allure.title('Тестируем авторизацию c несуществующим логином/паролем')
    @allure.description('Запрос должен вернуть в тексте ответа {"success": false} и код 401')
    @pytest.mark.parametrize('key', ['email', 'password'])
    def test_login_user(self, key):
        body = Helpers.mod_create_user_body()
        create_response = BurgersApi.create_user(body)
        login_body = body.copy()
        del login_body['name']
        login_body[key] += '1'

        login_response = BurgersApi.login_user(login_body)

        assert login_response.status_code == 401 and login_response.json()['success'] is False
        BurgersApi.delete_user(create_response.json()['accessToken'])
