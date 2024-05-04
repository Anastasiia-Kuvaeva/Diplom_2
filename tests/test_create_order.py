import allure

from utils.order_utils import OrderUtils
from data import (HttpStatuses, ErrorMessages)
from data import OrderData


# Тестовый набор создания заказа
class TestCreateOrder:

    @allure.title('Тест успешного создания заказа авторизованным пользователем')
    @allure.description('''Алгоритм тестирования: 
                1. Создание пользователя    
                2. Создание заказа  
                3. Проверка ответа
                4. Удаление ранее созданного пользователя''')
    def test_success_create_order(self, create_and_delete_new_user):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Создание заказа
        response = OrderUtils.create_order(token, OrderData.INGREDIENTS_VALID)
        # Проверка
        assert response.status_code == HttpStatuses.OK and response.json().get("success") == True

    @allure.title('Тест успешного создания заказа без авторизации')
    @allure.description('''Алгоритм тестирования: 
                    1. Создание заказа                       
                    2. Проверка ответа''')
    def test_success_create_order_without_auth(self):
        # Создание заказа
        response = OrderUtils.create_order(None, OrderData.INGREDIENTS_VALID)
        # Проверка
        assert response.status_code == HttpStatuses.OK and response.json().get("success") == True

    @allure.title('Тест невозможности создания заказа с невалидным хэшем ингредиента')
    @allure.description('''Алгоритм тестирования: 
                    1. Создание пользователя    
                    2. Попытка создание заказа  
                    3. Проверка ответа
                    4. Удаление ранее созданного пользователя''')
    def test_create_order_invalid_ingredients(self, create_and_delete_new_user):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Создание заказа
        response = OrderUtils.create_order(token, OrderData.INGREDIENTS_INVALID)
        # Проверка
        assert (response.status_code == HttpStatuses.INTERNAL_SERVER_ERROR
                and ErrorMessages.INTERNAL_SERVER_ERROR in response.text)

    @allure.title('Тест невозможности создания заказа без передачи ингредиентов')
    @allure.description('''Алгоритм тестирования: 
                        1. Создание пользователя    
                        2. Попытка создание заказа  
                        3. Проверка ответа
                        4. Удаление ранее созданного пользователя''')
    def test_create_order_empty_ingredients(self, create_and_delete_new_user):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Создание заказа
        response = OrderUtils.create_order(token, OrderData.INGREDIENTS_EMPTY)
        # Проверка
        assert (response.status_code == HttpStatuses.BAD_REQUEST
                and response.json().get("success") == False
                and response.json().get("message") == ErrorMessages.CREATE_ORDER_EMPTY_INGREDIENTS)
