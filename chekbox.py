"""Метод .check()

Специально для чекбоксов и радио.

Проверяет, что элемент именно input[type="checkbox"] или input[type="radio"].

Автоматически скроллит к элементу, если он не виден.

Ожидает, пока элемент станет интерактивным (если не использовать force=True).
import pytest
def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()"""

"""Метод .click()

Работает со всеми элементами, в том числе чекбоксами и радио.

Менее «умный» для чекбоксов, потому что просто имитирует клик.

Иногда может потребоваться скролл или ожидание вручную, если элемент скрыт.

Переписанный тест с .click():"""

def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()

"""💡 Вывод:

Для чекбоксов/радио лучше использовать .check() — код безопаснее и понятнее.

.click() универсален, но иногда может ломаться на скрытых элементах или кастомных компонентах."""