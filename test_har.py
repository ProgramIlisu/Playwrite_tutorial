from playwright.sync_api import sync_playwright

def record_har():

    with sync_playwright() as p:

        browser = p.chromium.launch(headed=True)

        context = browser.new_context(
            record_har_path="example.har"
        )

        page = context.new_page()

        page.goto(
            "https://reqres.in/",
            wait_until="domcontentloaded"
        )

        page.locator(
            'li[data-id="users-single"]'
        ).click()

        context.close()
        browser.close()