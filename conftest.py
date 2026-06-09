# Пример 1 — изменение viewport
# conftest.py
"""import pytest
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }"""

# Почему scope="session"?
# Чтобы контекст не пересоздавался для каждого теста.

# Пример 2 — установка cookies
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "stepik",
                    "value": "sd4fFfv!x_cfcstepik",
                    "domain": "example.com",
                    "path": "/",
                    "httpOnly": False,
                    "secure": False,
                }
            ]
        },
    } 



