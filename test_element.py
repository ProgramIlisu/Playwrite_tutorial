# versions pytest-9.0.2, python-3.11.9.final.0
from playwright.sync_api import expect
# Получить текст элемента через inner_text()
def test_inner_text(page):
    page.goto("https://zimaev.github.io/table/")
    expect(page.get_by_role("table", name="Список пользователей")).to_be_visible()
    element = page.get_by_role("cell", name="Mark")
    text = element.inner_text()
    assert "Mark" in text

# 📌 Возвращает видимый текст элемента.

#2️⃣ Получить текст через text_content()
def test_text_content(page):
    page.goto("https://zimaev.github.io/table/")
    expect(page.get_by_role("table", name="Список пользователей")).to_be_visible()
    element = page.get_by_role("cell", name="Mark")
    print(element.text_content())

# 📌 Возвращает весь текст, даже если он скрыт CSS.

# 3️⃣ Получить текст всех элементов (all_inner_texts())
# Например строки таблицы.

def test_all_inner_texts(page):
    page.goto("https://zimaev.github.io/table/")
    
    rows = page.locator("tr")
    print(rows.all_inner_texts())

# Результат: ['Name Age City', 'Anton 25 Moscow', 'Olga 30 Berlin']

#4️⃣ Получить текст всех элементов (all_text_contents())
def test_all_text_contents(page):
    page.goto("https://zimaev.github.io/table/")
    
    rows = page.locator("tr")
    print(rows.all_text_contents())

# Возвращает весь текст включая скрытый.

# 5️⃣ Получить HTML элемента
def test_inner_html(page):
    page.goto("https://zimaev.github.io/table/")

    element = page.locator("table")
    print(element.inner_html())

"""Вернет HTML внутри элемента.

Пример:

<span>playwright</span>
⚠️ Разница между inner_text() и text_content()
Метод	Что возвращает
inner_text()	только видимый текст
text_content()	весь текст, даже скрытый
all_inner_texts()	список видимых текстов
all_text_contents()	список всех текстов


💡 Частая задача QA (проверка текста)"""
def test_message(page):
    page.goto("https://example.com")

    message = page.locator("h1").inner_text()
    print(message)

    assert message == "Example Domain"


"""💡 Очень полезный совет для Playwright

Чтобы узнать правильный локатор, открой Inspector:

pytest --headed --slowmo 500 --debug test_element.py

или

playwright codegen https://zimaev.github.io/table/

и кликни на элемент — Playwright сам покажет правильный локатор.

Ключевая идея (запомни)

В Playwright:

.click() → действие → возвращает None

.inner_text() → возвращает видимый текст

.text_content() → возвращает весь текст (включая скрытый)

💡 Мини-шпаргалка
locator = page.get_by_role("cell", name="Mark")

locator.click()              # действие
text1 = locator.inner_text() # текст (видимый)
text2 = locator.text_content() # текст (весь)


Запускай тесты с флагом:

pytest -s --headed test_element.py
🔍 Что делает -s

отключает захват вывода (stdout/stderr)

показывает все print() прямо в терминале

"""