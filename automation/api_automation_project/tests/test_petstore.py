from clients.petstore_client import APIClient

def test_create_user_success():
    client = APIClient()
    
    # Шаг 1: Отправляем запрос на создание пользователя "Ivan"
    response = client.create_user("Ivan", "QA Engineer")
    
    # Проверка 1: Статус-код ответа равен 201 (Created)
    assert response.status_code == 201
    
    # Проверка 2: В ответе сервера имя соответствует отправленному
    response_data = response.json()
    assert response_data["name"] == "Ivan"
    assert response_data["job"] == "QA Engineer"
    # Проверяем, что сервер сгенерировал ID для нового пользователя
    assert "id" in response_data


def test_get_user_not_found():
    client = APIClient()
    
    # Шаг 1: Запрашиваем несуществующего пользователя (например, ID 23)
    response = client.get_user(23)
    
    # Проверка: Статус-код должен быть 404 (Not Found)
    assert response.status_code == 404