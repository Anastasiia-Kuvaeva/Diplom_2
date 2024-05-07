import pytest
import allure

from utils.user_utils import UserUtils
from data import (HttpStatuses, ErrorMessages)
from helpers import UserData


# Тестовый набор изменения пользователя
class TestChangeUserData:

    @allure.title('Тест успешного изменения данных с авторизацией')
    @allure.description('''Алгоритм тестирования: 
                1. Создание пользователя   
                2. Изменение данных пользователя   
                3. Проверка ответа
                4. Удаление ранее созданного пользователя''')
    @pytest.mark.parametrize('edit_data', [
        {'email': UserData.generation_valid_data_for_create_user()['email']},
        {'password': UserData.generation_valid_data_for_create_user()["password"]},
        {'name': UserData.generation_valid_data_for_create_user()["name"]}
    ])
    def test_edit_user(self, create_and_delete_new_user, edit_data):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Изменение данных пользователя
        response = UserUtils.edit_user(token, edit_data)
        # Проверка
        assert response.status_code == HttpStatuses.OK and response.json().get("success") == True

    @allure.title('Тест невозможности изменения данных пользователя без авторизации')
    @allure.description('''Алгоритм тестирования:                    
                    1. Попытка изменения данных пользователя без авторизации
                    2. Проверка ответа''')
    @pytest.mark.parametrize('edit_data', [
        {'email': UserData.generation_valid_data_for_create_user()['email']},
        {'password': UserData.generation_valid_data_for_create_user()["password"]},
        {'name': UserData.generation_valid_data_for_create_user()["name"]}
    ])
    def test_change_person_data_whithout_auth(self, edit_data):
        # Попытка изменения данных пользователя без авторизации
        response = UserUtils.edit_user(None, edit_data)
        # Проверка
        assert (response.status_code == HttpStatuses.UNAUTHORIZED
                and response.json().get("message") == ErrorMessages.UNAUTHORIZED)
