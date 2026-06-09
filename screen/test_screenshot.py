# Базовый скриншот страницы (самый частый кейс)
def test_screenshot(page):
    page.goto("https://zimaev.github.io/table/")
    page.screenshot(path="screen/screenshot.png")

# Создаст файл: screenshot.png в корне проекта.

# 2️⃣ Скриншот всей страницы (full page)
# Используется, когда страница длинная (скролл).

def test_full_page_screenshot(page):
    page.goto("https://zimaev.github.io/table/")
    page.screenshot(
        path="screen/full_page.png",
        full_page=True
    )
# 3️⃣ Скриншот конкретного элемента (очень популярно в UI-тестах)
def test_element_screenshot(page):
    page.goto("https://zimaev.github.io/table/")

    element = page.get_by_role("table")
    element.screenshot(path="screen/table.png")

"""Это стандартный паттерн для:

проверки верстки
фиксации бага
вложения в отчёт

4) Скриншот области (clip)
Используется редко, но важно знать: """

def test_screenshot_area(page):
    page.goto("https://zimaev.github.io/table/")
    page.screenshot(
        path="screen/clip.png",
        clip={
            "x": 50,
            "y": 0,
            "width": 400,
            "height": 300
        }
)
# 6️⃣ JPEG с качеством
def test_screenshot_JPEG(page):
    page.goto("https://zimaev.github.io/table/")
    page.screenshot(
        path="screen/image.jpeg",
        type="jpeg",
        quality=80
)

"""Важно:

quality работает только с jpeg
7️⃣ Прозрачный фон (UI/дизайн тесты)"""
def test_screenshot_transparent(page):
    page.goto("https://zimaev.github.io/table/")    
    page.screenshot(
        path="screen/transparent.png",
        omit_background=True
)

