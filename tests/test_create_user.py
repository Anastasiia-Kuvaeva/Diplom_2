import pytest
import allure

from utils.user_utils import UserUtils
from data import (HttpStatuses, ErrorMessages)
from data import UserData


# Тестовый набор создания пользователя
class TestCreateUser:

    @allure.title('Тест успешного создания уникального пользователя')
    @allure.description('''Алгоритм тестирования: 
            1. Создание пользователя      
            2. Проверка ответа
            3. Удаление ранее созданного пользователя''')
    def test_success_create_user(self, create_and_delete_new_user):
        # Создание пользователя
        response = create_and_delete_new_user[1]
        # Проверка
        assert response.status_code == HttpStatuses.OK and response.json().get("success") == True

    @allure.title('Тест невозможности создания существующего пользователя')
    @allure.description('''Алгоритм тестирования: 
                1. Создание пользователя
                2. Попытка повторного создание пользователя с теми же данными   
                3. Проверка ответа
                4. Удаление ранее созданного пользователя''')
    def test_create_exists_user(self, create_and_delete_new_user):
        # Создание пользователя
        payload = create_and_delete_new_user[0]
        # Попытка повторного создание пользователя с теми же данными
        response = UserUtils.create_user(payload)
        # Проверка
        assert (response.status_code == HttpStatuses.FORBIDDEN
                and response.json().get("success") == False
                and response.json().get("message") == ErrorMessages.CREATE_EXISTS_USER)

    @allure.title('Тест невозможности создания пользователя с некорректными данными')
    @allure.description('''Алгоритм тестирования: 
                    1. Попытка создание пользователя с некорректными данными
                    2. Проверка ответа''')
    @pytest.mark.parametrize('absent_field', ['email', 'password', 'name'])
    def test_create_user_incorrect_data(self, absent_field):
        # Получение данных для создания пользователя
        payload = UserData.generation_valid_data_for_create_user()
        # Удаление поля
        del payload[absent_field]
        # Попытка создание пользователя с некорректными данными
        response = UserUtils.create_user(payload)
        # Проверка
        assert (response.status_code == HttpStatuses.FORBIDDEN
                and response.json().get("success") == False
                and response.json().get("message") == ErrorMessages.CREATE_USER_INCORRECT_DATA)
