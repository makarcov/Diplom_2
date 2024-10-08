import allure
import pytest

from burgers_api import BurgersApi
from data import ExpectedAnswers
from helpers import Helpers


class TestCreateUser:

    @allure.title('Тестируем создание нового пользователя')
    @allure.description('Запрос должен вернуть {"success": true} и код 200')
    def test_create_user(self):
        create_response = BurgersApi.create_user(Helpers.mod_create_user_body())

        assert create_response.status_code == 200 and create_response.json()['success'] is True
        BurgersApi.delete_user(create_response.json()['accessToken'])

    @allure.title('Тестируем создание двух одинаковых пользователей')
    @allure.description('Запрос должен вернуть ошибку и код 403')
    def test_create_two_identical_users(self):
        body = Helpers.mod_create_user_body()
        create_user = BurgersApi.create_user(body)
        create_identical_user_response = BurgersApi.create_user(body)
        expected_text = ExpectedAnswers.CREATE_TWO_IDENTICAL_USERS

        assert create_identical_user_response.status_code == 403 and create_identical_user_response.json()['message'] == expected_text
        BurgersApi.delete_user(create_user.json()['accessToken'])

    @allure.title('Тестируем создание пользователя с незаполненным обязательным полем')
    @allure.description('Запрос должен вернуть ошибку и код 403')
    @pytest.mark.parametrize('key', ['email', 'password', 'name'])
    def test_create_new_user_with_empty_field(self, key):
        body = Helpers.mod_create_user_body()
        body[key] = ""
        create_response = BurgersApi.create_user(body)
        expected_response_text = ExpectedAnswers.CREATE_USER_WITH_EMPTY_FIELD

        assert create_response.status_code == 403 and create_response.json()['message'] == expected_response_text
