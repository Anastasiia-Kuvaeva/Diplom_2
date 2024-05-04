# Данные для тестов
from faker import Faker


# HTTP-статусы
class HttpStatuses:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500


# Сообщения об ошибках
class ErrorMessages:
    CREATE_EXISTS_USER = 'User already exists'
    CREATE_USER_INCORRECT_DATA = 'Email, password and name are required fields'
    CREATE_ORDER_EMPTY_INGREDIENTS = 'Ingredient ids must be provided'
    INTERNAL_SERVER_ERROR = 'Internal Server Error'
    UNAUTHORIZED = 'You should be authorised'


# Данные пользователя
class UserData:

    # Генерация валидных данных для регистрации пользователя
    @staticmethod
    def generation_valid_data_for_create_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data


# Данные заказа
class OrderData:
    # Корректные ингредиенты
    INGREDIENTS_VALID = {
        "ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
    }

    # Некорретные ингредиенты
    INGREDIENTS_INVALID = {
        "ingredients": ["0000b41abdacsdf6a70000", "111146e4dcsfdf0276b1111"]
    }

    # Пустые ингредиенты
    INGREDIENTS_EMPTY = {
        "ingredients": []
    }
