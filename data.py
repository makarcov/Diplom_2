class Url:

    BASE_URL = 'https://stellarburgers.nomoreparties.site'


class Body:

    CREATE_USER_BODY = {
        "email": "test-data@yandex.ru",
        "password": "password",
        "name": "Username"
    }

    CREATE_ORDER_BODY = {
        "ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
    }

    CREATE_ORDER_BODY_INVALID = {
        "ingredients": ["60d3b41abdacab0026a733c698765"]
    }


class ExpectedAnswers:

    CREATE_TWO_IDENTICAL_USERS = 'User already exists'
    CREATE_USER_WITH_EMPTY_FIELD = 'Email, password and name are required fields'

    LOGIN_USER_WITH_WRONG_LOG_PASS = 'email or password are incorrect'

    UPDATE_INFO_WITHOUT_AUTH = 'You should be authorised'

    ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'

    GET_USER_ORDER_LIST_WITHOUT_AUTH = 'You should be authorised'
