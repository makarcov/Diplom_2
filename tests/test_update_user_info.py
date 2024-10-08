import allure
import pytest

from burgers_api import BurgersApi
from data import ExpectedAnswers
from helpers import Helpers


class TestUpdateUserInfo:

    @allure.title('Тестируем изменение данных у авторизированного пользователя')
    @allure.description('Запрос должен вернуть в тексте ответа {"success": true} и код 200')
    @pytest.mark.parametrize('key', ['email', 'password', 'name'])
    def test_update_info_auth_user(self, key):
        body = Helpers.mod_create_user_body()
        create_response = BurgersApi.create_user(body)
        token = create_response.json()['accessToken']
        BurgersApi.login_user(body)
        update_body = body.copy()
        update_body.clear()
        update_body[key] = body[key] + '777'
        update_info_response = BurgersApi.update_user_info(update_body, token)

        assert update_info_response.status_code == 200 and update_info_response.json()['success'] is True
        BurgersApi.delete_user(token)

    @allure.title('Тестируем изменение данных у неавторизированного пользователя')
    @allure.description('Запрос должен вернуть в тексте ответа {"success": false} и код 401')
    @pytest.mark.parametrize('key', ['email', 'password', 'name'])
    def test_update_info_without_auth(self, key):
        body = Helpers.mod_create_user_body()
        create_response = BurgersApi.create_user(body)
        token = create_response.json()['accessToken']
        update_body = body.copy()
        update_body.clear()
        update_body[key] = body[key] + '777'
        update_info_response = BurgersApi.update_user_info(update_body, token=None)

        assert update_info_response.status_code == 401 and update_info_response.json()['success'] is False \
               and update_info_response.json()['message'] == ExpectedAnswers.UPDATE_INFO_WITHOUT_AUTH
        BurgersApi.delete_user(token)
