from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Локаторы
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('button[type="submit"]')
        # self.error_message = page.locator('#flash')
        self.error_message = page.locator('#errorAlert')

    # Открытие страницы
    def open(self):
        # self.page.goto("https://the-internet.herokuapp.com/login")
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

    # Ввод имени пользователя
    def enter_username(self, username: str):
        self.username_input.fill(username)

    # Ввод пароля
    def enter_password(self, password: str):
        self.password_input.fill(password)

    # Нажатие кнопки логина
    def click_login(self):
        self.login_button.click()

    # Полная авторизация
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Получение текста ошибки
    def get_error_message(self):
        # return self.error_message.text_content()
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()

# Главное отличие
# text_content()

# Возвращает: textContent из DOM. Берёт текст как он есть в HTML.

# Включает:
# скрытый текст
# переносы
# лишние пробелы
# текст невидимых элементов

# inner_text()
# Возвращает: видимый текст как в браузере. То есть то, что реально видит пользователь.

# Учитывает:
# CSS
# visibility
# display:none
# форматирование