import allure

from utils.order_utils import OrderUtils
from data import (HttpStatuses, ErrorMessages)
from data import OrderData


# Тестовый набор получения заказов
class TestGetOrder:

    @allure.title('Тест успешного получения заказов авторизованным пользователем')
    @allure.description('''Алгоритм тестирования: 
                1. Создание пользователя      
                2. Создание заказа
                3. Получение заказа
                4. Проверка ответа
                5. Удаление ранее созданного пользователя''')
    def test_success_get_order_list_whith_auth(self, create_and_delete_new_user):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Создание заказа
        response_create_order = OrderUtils.create_order(token, OrderData.INGREDIENTS_VALID)
        # Получение заказов пользователя
        response_get_order_list = OrderUtils.get_order_list(token)
        # Проверка
        assert (response_get_order_list.status_code == HttpStatuses.OK
                and response_get_order_list.json().get("success") == True
                and response_create_order.json()["order"]["number"] == response_get_order_list.json()["orders"][0][
                    "number"])

    @allure.title('Тест невозможности получения заказов неавторизованным пользователем')
    @allure.description('''Алгоритм тестирования: 
                    1. Попытка получения заказов неавторизованным пользователем                       
                    2. Проверка ответа''')
    def test_get_order_list_whithout_auth(self):
        # Получение заказов пользователя
        response = OrderUtils.get_order_list(None)
        # Проверка
        assert (response.status_code == HttpStatuses.UNAUTHORIZED
                and response.json().get("success") == False
                and response.json().get("message") == ErrorMessages.UNAUTHORIZED)
