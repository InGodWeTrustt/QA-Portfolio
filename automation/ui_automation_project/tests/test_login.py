from pages.login_page import LoginPage

def test_succesful_login(page):
    login_page = LoginPage(page)

    # Шаг 1. Переход на сайт
    login_page.navigate()
    
    # Шаг 2: Вводим валидные данные (встроенный фикстурный юзер сайта)
    login_page.login("standard_user", "secret_sauce")
    
    # Проверка: URL изменился на страницу каталога товаров
    assert page.url == "https://saucedemo.com" 

def test_failed_login(page):
    login_page = LoginPage(page)
    
    # Шаг 1: Открываем сайт
    login_page.navigate()
    
    # Шаг 2: Вводим неверный пароль
    login_page.login("standard_user", "wrong_password")
    
    # Проверка: Появилось сообщение об ошибке
    error_text = login_page.get_error_message()
    assert "Username and password do not match any user in this service" in error_text