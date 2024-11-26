import random


class UserDataGenerate:
    @staticmethod
    def get_random_user_data():
        return {
            "email": 'email_' + str(random.randint(10000, 99999)) + '@yandex.ru',
            "password": 'password_' + str(random.randint(10000, 99999)),
            "name": 'name_' + str(random.randint(10000, 99999))
        }


