import pytest
import allure


@allure.feature('Авторизация')
@allure.story('Недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с недействительными учетными данными')
def test_login_failure(login_page):

    with allure.step('Открыть страницу авторизации'):
        login_page.open()

    with allure.step('Ввести неверные учетные данные'):
        login_page.login('invalid_user', 'invalid_password')

    with allure.step('Проверить отображение ошибки'):
        assert "Invalid credentials" in \
               login_page.get_error_message()


@allure.feature('Авторизация')
@allure.story('Корректные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с корректными учетными данными')
@pytest.mark.parametrize('username, password',
    [('user', 'user'), ('admin', 'admin')]
)
def test_login_success(login_page, dashboard_page, username, password):

    with allure.step('Открыть страницу авторизации'):
        login_page.open()

    with allure.step(f'Авторизоваться как {username}'):
        login_page.login(username, password)

    with allure.step('Проверить приветственное сообщение'):
        dashboard_page.assert_welcome_message(f'Welcome {username}')