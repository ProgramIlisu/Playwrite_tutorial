# 1) Выбор по value
def test_select_by_value(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option("#floatingSelect", value="3")

#Что происходит:
#<option value="3">У меня лапки</option>
#Выбирается этот пункт.


# 2) Выбор по index
# Индексация начинается с 0.

def test_select_by_index(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option("#floatingSelect", index=1)

#Это выберет:
#<option value="2">Предложил новую функцию</option>

# 3)Выбор по label (по тексту)
def test_select_by_label(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option("#floatingSelect", label="Нашел и завел bug")

#Playwright ищет текст внутри <option>.


# 4) Короткая запись (по value)
#По умолчанию используется value.

def test_select_short(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option("#floatingSelect", "3")

#Это то же самое, что:
#value="3"


# 5) Множественный выбор (multiple select)
#Если <select multiple>.

def test_select_multiple(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option("#skills", value=["playwright", "python"])

#Playwright выберет две опции одновременно.

# 6)  Более правильный вариант через locator

#Рекомендуется писать так:

def test_select_locator(page):
    page.goto("https://zimaev.github.io/select/")
    
    dropdown = page.locator("#floatingSelect")
    dropdown.select_option(value="2")

# Это лучше для Page Object Model.

# ▶️ Как запускать

# В папке проекта:
# pytest --headed

#или с инспектором:

#set PWDEBUG=1
#pytest

# 💡 Полезный факт для тестировщика:
#select_option() работает только с <select>, но не работает с кастомными dropdown (React, Angular).
#Там используется обычный click().

#Если хочешь, я покажу 3 самые частые ошибки с dropdown в Playwright, на которых валятся почти все начинающие QA.





