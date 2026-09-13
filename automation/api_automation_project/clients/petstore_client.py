import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://reqres.in"

    def create_user(self, name, job):
        """Отправляет POST-запрос на создание пользователя"""
        payload = {
            "name": name,
            "job": job
        }
        # Отправляем запрос и возвращаем ответ сервера
        response = requests.post(f"{self.base_url}/users", json=payload)
        return response

    def get_user(self, user_id):
        """Отправляет GET-запрос на получение данных пользователя"""
        response = requests.get(f"{self.base_url}/users/{user_id}")
        return response
