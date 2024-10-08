import pytest

from burgers_api import BurgersApi
from helpers import Helpers


# создаем нового пользователя, после выполнения теста он удаляется
@pytest.fixture(scope='function')
def new_user():
    body = Helpers.mod_create_user_body()
    user = BurgersApi.create_user(body)
    token = user.json()['accessToken']

    yield user

    BurgersApi.delete_user(token)
