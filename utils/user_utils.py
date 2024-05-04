# Вспомогательные методы для работы с пользователями
import allure
import requests

from config import Urls


class UserUtils:
    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(data):
        return requests.post(Urls.CREATE_USER_URL, data=data)

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        return requests.delete(Urls.DELETE_USER_URL, headers={"Authorization": token})

    @staticmethod
    @allure.step('Редактирование пользователя')
    def edit_user(token, data):
        return requests.patch(Urls.USER_EDIT_URL, headers={"Authorization": token}, data=data)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(data):
        return requests.post(Urls.LOGIN_USER_URL, data=data)
