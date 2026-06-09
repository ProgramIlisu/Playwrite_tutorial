import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.get_by_text("Создать первый сценарий playwright")).to_be_visible()


 # with sync_playwright() as playwright:
 #   run(playwright)
