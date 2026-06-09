# 🎭 Playwright UI Automation Project

**Автоматизация UI-тестирования с использованием Playwright, Pytest и Allure Report**

---

## 🚀 О проекте

Данный проект демонстрирует современные подходы к автоматизации тестирования веб-приложений с использованием:

* 🎭 Playwright
* 🧪 Pytest
* 📊 Allure Report
* 🏗️ Page Object Model (POM)
* ⚙️ Fixtures
* 🔄 Parameterized Tests

Проект разработан в учебных целях для изучения автоматизации UI-тестирования на Python.

---

## 🛠️ Технологический стек

| Технология    | Назначение                    |
| ------------- | ----------------------------- |
| Python        | Основной язык разработки      |
| Playwright    | UI-автоматизация              |
| Pytest        | Фреймворк тестирования        |
| Allure Report | Формирование отчётов          |
| POM           | Архитектура тестового проекта |

---

## 📂 Структура проекта

```text
Playwrite_project/
│
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_login.py
│
├── reports/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ✨ Реализованный функционал

### 🔐 Авторизация

* Проверка успешного входа
* Проверка обработки неверных учётных данных
* Проверка приветственного сообщения

### 🏗️ Page Object Model

Для каждой страницы создан отдельный класс:

* `LoginPage`
* `DashboardPage`

Это позволяет:

✅ переиспользовать код

✅ уменьшить количество дублирования

✅ повысить читаемость тестов

✅ упростить поддержку проекта

---

## ⚡ Установка проекта

### Клонирование репозитория

```bash
git clone https://github.com/ProgramIlisu/Playwrite_project.git
cd Playwrite_project
```

### Создание виртуального окружения

```bash
python -m venv .venv
```

### Активация

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Установка браузеров Playwright

```bash
playwright install
```

---

## ▶️ Запуск тестов

### Все тесты

```bash
pytest
```

### С отображением браузера

```bash
pytest -s --headed
```

### Конкретный тест

```bash
pytest tests/test_login.py
```

---

## 📊 Allure Report

### Генерация результатов

```bash
pytest --alluredir=reports
```

### Просмотр отчёта

```bash
allure serve reports
```

---

## 🧪 Пример параметризованного теста

```python
@pytest.mark.parametrize(
    "username, password",
    [
        ("admin", "admin")
    ]
)
def test_login_success(
        login_page,
        dashboard_page,
        username,
        password
):
    login_page.open()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(
        f"Welcome {username}"
    )
```

---

## 📈 Что изучено в проекте

* Работа с Playwright
* Локаторы и взаимодействие с элементами
* Page Object Model
* Fixtures Pytest
* Параметризация тестов
* Allure-аннотации
* Формирование отчётов
* Организация структуры UI-проекта

---

## 🎯 Планы по развитию

* [ ] GitHub Actions CI/CD
* [ ] Скриншоты при падении тестов
* [ ] Видео выполнения тестов
* [ ] API-тестирование
* [ ] Docker-конфигурация
* [ ] Кроссбраузерное тестирование

---

## 👨‍💻 Автор

**Denis (ProgramIlisu)**

⭐ Если проект оказался полезным — поставьте звезду репозиторию.
