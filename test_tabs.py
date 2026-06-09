# 1️⃣ Базовый рабочий тест открытия новой вкладки
from playwright.sync_api import expect

def test_new_tab(page):
    page.goto("https://zimaev.github.io/tabs/")

    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value

    expect(new_tab).to_have_url(
        "https://zimaev.github.io/tabs/dashboard/index.html?"
    )

    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    expect(sign_out).to_be_visible()


"""Что здесь происходит (по шагам)
with page.context.expect_page() as tab:

👉 говорим Playwright:

жду открытие новой вкладки
page.get_by_text("Переход к Dashboard").click()

👉 триггер открытия новой вкладки

new_tab = tab.value

👉 получаем объект:

Page новой вкладки
Важно: почему используется context

В архитектуре Playwright:

Browser
   └── Context
          ├── Page (вкладка 1)
          └── Page (вкладка 2)

Поэтому:

page.context.expect_page()

а не:

page.expect_page()   ❌

2️⃣ Частая ошибка новичков

Неправильно:

page.get_by_text("Переход к Dashboard").click()
new_tab = page.context.expect_page()

Ошибка:

вкладка уже открылась — ожидание началось слишком поздно
3️⃣ Проверка URL — лучше через expect

Вместо:

assert new_tab.url == "..."

лучше:

expect(new_tab).to_have_url("...")

Почему:

ждёт загрузку страницы
стабильнее
меньше flaky тестов
4️⃣ Если нужно переключиться на вкладку и работать дальше
new_tab.fill("#username", "admin")
new_tab.fill("#password", "123")
new_tab.click("button")

Это уже полноценная работа с новой вкладкой."""

#5️⃣ Второй пример — вкладка с Alert

from playwright.sync_api import expect

def test_new_tab_alert(page):
    page.goto("https://zimaev.github.io/tabs/")

    with page.expect_popup() as tab:
        page.get_by_role("button", name="Переход к allert").click()
        
    new_tab = tab.value

    expect(new_tab).to_have_url(
    "https://zimaev.github.io/tabs/modal/modal.html?"
    )
    