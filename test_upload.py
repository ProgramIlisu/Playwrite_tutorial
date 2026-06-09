"""Самый простой способ — set_input_files()

Это самый используемый способ."""

from playwright.sync_api import Page

def test_upload_file(page: Page):
    page.goto("https://zimaev.github.io/upload/")
    page.set_input_files("#formFile", "Установка_Playwright.txt")

"""Что происходит:
Playwright находит <input type="file">
загружает файл hello.txt
нажимает кнопку отправки

2️⃣ Через событие filechooser
Playwright ловит событие выбора файла."""

def test_upload_file_event(page: Page):
    page.goto("https://zimaev.github.io/upload/")
    
    page.on("filechooser", lambda fc: fc.set_files("Установка_Playwright.txt"))
    
    page.locator("#formFile").click()

# Когда открывается окно выбора файла — Playwright автоматически подставляет файл.

"""3️⃣ Через expect_file_chooser() (более правильный вариант)

Этот способ чаще используют в реальных проектах."""

def test_upload_file_expect(page: Page):
    page.goto("https://zimaev.github.io/upload/")
    
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    
    file_chooser = fc_info.value
    file_chooser.set_files("Установка_Playwright.txt")

"""⚠️ Частая ошибка

Если файл не найден:

Error: ENOENT no such file or directory

значит файл:

hello.txt

лежит не в той папке.

Правильная структура:

Playwrite_tutorial
│
├── test_upload.py
└── hello.txt
▶️ Запуск теста
pytest --headed

или

pytest -k upload

💡 Полезно знать QA:

set_input_files() можно загружать несколько файлов:

page.set_input_files("#formFile", ["file1.txt", "file2.txt"])"""