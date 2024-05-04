# Вспомогательные методы для работы с заказами
import allure
import requests

from config import Urls


class OrderUtils:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(token, data):
        return requests.post(Urls.CREATE_ORDER_URL, headers={"Authorization": token}, data=data)

    @staticmethod
    @allure.step('Получение заказов')
    def get_order_list(token):
        return requests.get(Urls.GET_ORDER_LIST_URL, headers={"Authorization": token})
