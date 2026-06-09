import pytest

def test_chain_with_double_arrow(page):
    page.goto("https://zimaev.github.io/navbar/")
    page.locator("#navbarNavDropdown >> li:has-text('Company')").click()
    
def test_chain_with_variable(page):
    page.goto("https://zimaev.github.io/navbar/")
    nav_bar = page.locator("div#navbarNavDropdown")
    nav_bar.locator("li:has-text('Company')").click()   

def test_filter_has_text(page):
    page.goto("https://zimaev.github.io/navbar/")

    page.locator("li").filter(has_text="Company").click()

def test_filter_has_locator(page):
    page.goto("https://zimaev.github.io/navbar/")

    page.locator("li").filter(
        has=page.locator(".dropdown-toggle")
    ).first.click()

def test_filter_has_not(page):
    page.goto("https://zimaev.github.io/filter/")

    rows = page.locator("tr")

    count = rows.filter(
        has_not=page.get_by_role("button")
    ).count()

    print(count)

def test_filter_has_not_text(page):
    page.goto("https://zimaev.github.io/filter/")

    rows = page.locator("tr")

    rows.filter(
        has_not_text="helicopter"
    ).first.click()
    