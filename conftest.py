import pytest
from data import UserData
from utils.user_utils import UserUtils


# Фикстура создания м последующего удаления пользователя
@pytest.fixture
def create_and_delete_new_user():
    # Генерация данных нового пользователя
    payload = UserData.generation_valid_data_for_create_user()
    # Создание нового пользователя
    response = UserUtils.create_user(payload)
    yield payload, response
    # Удаление пользователя
    UserUtils.delete_user(response.json()["accessToken"])
