import allure

from utils.user_utils import UserUtils
from data import (HttpStatuses)
from helpers import UserData


# Тестовый набор логина пользователя
class TestLoginUser:

    @allure.title('Тест успешной авторизации существующего пользователя')
    @allure.description('''Алгоритм тестирования: 
                1. Создание пользователя  
                2. Авторизация пользователя    
                3. Проверка ответа
                4. Удаление ранее созданного пользователя''')
    def test_success_login_user(self, create_and_delete_new_user):
        # Создание пользователя
        payload = create_and_delete_new_user[0]
        # Авторизация ранее созданного пользователя
        response = UserUtils.login_user(payload)
        # Проверка
        assert (response.status_code == HttpStatuses.OK
                and response.json().get("success") == True
                and 'accessToken' in response.text
                and 'refreshToken"' in response.text)

    @allure.title('Тест невозможности авторизации под несуществующим пользователем')
    @allure.description('''Алгоритм тестирования: 
                        1. Попытка авторизации под несуществующим пользователем
                        2. Проверка ответа''')
    def test_login_not_exists_user(self):
        # Генерация случайных данных пользователя
        payload = UserData.generation_valid_data_for_create_user()
        # Попытка авторизации под несуществующим пользователем
        response = UserUtils.login_user(payload)
        # Проверка
        assert response.status_code == HttpStatuses.UNAUTHORIZED and response.json().get("success") == False
