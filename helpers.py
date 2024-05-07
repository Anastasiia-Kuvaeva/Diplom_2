from faker import Faker


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
