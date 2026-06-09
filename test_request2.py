from playwright.sync_api import Page
def test_block_resources(page):
    page.route("**/*.{png,jpg,jpeg,gif,svg,woff,woff2}", lambda route: route.abort())
    page.goto("https://example.com")