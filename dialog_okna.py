#Без обработки диалогов (Playwright закрывает автоматически)
from playwright.sync_api import Page

def test_dialogs_auto(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()

#По умолчанию Playwright сам закрывает диалоги.

#2️⃣ Alert (нажать OK)
#alert имеет только кнопку OK.

def test_alert(page: Page):
    page.goto("https://zimaev.github.io/dialog/")

    page.on("dialog", lambda dialog: dialog.accept())

    page.get_by_text("Диалог Alert").click()

#Метод: dialog.accept()
#нажимает OK.

#3️⃣ Confirm (OK)
def test_confirm_ok(page: Page):
    page.goto("https://zimaev.github.io/dialog/")

    page.on("dialog", lambda dialog: dialog.accept())

    page.get_by_text("Диалог Confirmation").click()

# Результат на странице: Изменения сохранены!

#4️⃣ Confirm (Cancel)
def test_confirm_cancel(page: Page):
    page.goto("https://zimaev.github.io/dialog/")

    page.on("dialog", lambda dialog: dialog.dismiss())

    page.get_by_text("Диалог Confirmation").click()

#Метод: dialog.dismiss()
#нажимает Cancel / Отмена.

#5️⃣ Prompt (ввод текста)
#prompt позволяет ввести текст.

def test_prompt(page: Page):
    page.goto("https://zimaev.github.io/dialog/")

    page.on("dialog", lambda dialog: dialog.accept("Playwright QA"))

    page.get_by_text("Диалог Prompt").click()

# Playwright введет: Playwright QA

# 6️⃣ Получить текст диалога
# Можно проверить сообщение в окне.

def test_dialog_message(page: Page):
    page.goto("https://zimaev.github.io/dialog/")

    def handle_dialog(dialog):
        print(dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)

    page.get_by_text("Диалог Alert").click()

#Метод:

#dialog.message - возвращает текст диалога.

# 7️⃣ Обработать диалог только один раз
def test_dialog_once(page: Page):
    page.goto("https://zimaev.github.io/dialog/")

    page.once("dialog", lambda dialog: dialog.accept())

    page.get_by_text("Диалог Alert").click()

"""once() — слушатель сработает только один раз.

⚠️ Важное правило

Если используется:

page.on("dialog", ...)

обязательно должен быть:

dialog.accept()

или

dialog.dismiss()

Иначе тест зависнет, потому что окно будет ждать действие.

💡 Полезно знать для тестировщика:

Тип	Кнопки	Что делает
alert	OK	сообщение
confirm	OK / Cancel	подтверждение
prompt	поле ввода	ввод данных"""