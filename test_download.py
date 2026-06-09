# Полный код теста скачивания файла
import os
from playwright.sync_api import Page

def test_download(page: Page):

    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download").click()

    download = download_info.value

    file_name = download.suggested_filename
    destination_folder_path = "./data"

    os.makedirs(destination_folder_path, exist_ok=True)

    download.save_as(os.path.join(destination_folder_path, file_name))
"""
Что делает код
1️⃣ Открывает страницу
page.goto("https://demoqa.com/upload-download")

2️⃣ Ждет событие скачивания
with page.expect_download() as download_info:
Playwright ожидает начало загрузки файла.

3️⃣ Нажимает кнопку скачивания
page.locator("a:has-text('Download')").click()

4️⃣ Получает объект загрузки
download = download_info.value

Теперь можно работать с файлом.

5️⃣ Получает имя файла
file_name = download.suggested_filename

Например:

sampleFile.jpeg
6️⃣ Создает папку
os.makedirs(destination_folder_path, exist_ok=True)

Создаст папку data, если её нет.

7️⃣ Сохраняет файл
download.save_as(os.path.join(destination_folder_path, file_name))

Файл будет сохранен:

project/
 ├ test_download.py
 └ data/
    └ sampleFile.jpeg
Как запускать тест
pytest --headed test_download.py

или медленно:

pytest --headed --slowmo 1000 test_download.py
Полезные методы объекта download
Метод	Что делает
download.path()	путь временного файла
download.url	URL скачивания
download.suggested_filename	имя файла
download.save_as()	сохранить файл
download.delete()	удалить файл
download.failure()	ошибка загрузки

💡 Полезный трюк для QA:
после скачивания можно проверить, что файл реально существует:

assert os.path.exists(os.path.join(destination_folder_path, file_name))"""