from playwright.sync_api import sync_playwright
from pageclass import LoginPage


def test_login_failure(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login("invalid_user", "invalid_password")

    assert "Invalid credentials" in login_page.get_error_message()


""" def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.open()
        login_page.login("admin", "123456")

        browser.close()"""