from playwright.sync_api import expect

def test_todo(page):
    # Шаг 1: открыть сайт
    page.goto('https://demo.playwright.dev/todomvc/#/')
    page.pause()
    
    # Шаг 2: проверить корректный URL
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    
    # Шаг 3: найти поле ввода задачи
    input_field = page.get_by_placeholder('What needs to be done?')
    
    # Шаг 4: проверить, что поле пустое
    expect(input_field).to_be_empty()
    
    # Шаг 5: ввести первую задачу
    input_field.fill("Закончить курс по playwright")
    input_field.press('Enter')
    page.pause()
    
    # Шаг 6: ввести вторую задачу
    input_field.fill("Добавить в резюме, что умею автоматизировать")
    input_field.press('Enter')
    
    # Шаг 7: проверить, что количество задач равно двум
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    
    # Шаг 8: отметить первую задачу выполненной
    todo_item.get_by_role('checkbox').nth(0).click()
    
    # Шаг 9: проверить, что задача отмечена как выполненная
    expect(todo_item.nth(0)).to_have_class('completed')