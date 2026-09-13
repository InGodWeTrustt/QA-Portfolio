class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def navigate(self):
        """Открывает страницу логина"""
        self.page.goto("https://saucedemo.com")

    def login(self, username, password):
        """Заполняет форму и нажимает кнопку Войти"""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        """Возвращает текст ошибки, если она есть"""
        return self.page.locator(self.error_message).text_content()