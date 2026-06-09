from playwright.sync_api import Page, Route, expect

def test_intercepted(page: Page):

    page.route(
        "**/api/tags",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            json={
                "tags": [
                    "open",
                    "solutions"
                ]
            }
        )
    )

    page.goto("https://demo.realworld.io/")

    sidebar = page.locator("div.sidebar")

    expect(
        sidebar.get_by_role("link")
    ).to_contain_text([
        "open",
        "solutions"
    ])