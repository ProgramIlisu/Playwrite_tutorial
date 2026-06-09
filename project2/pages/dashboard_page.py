from playwright.sync_api import Page, expect


class DashboardPage:

    def __init__(self, page: Page):

        self.page = page

        # локаторы
        self.profile = page.locator('#usernameDisplay')
        self.logout = page.locator('#logout')

    def assert_welcome_message(self, message: str):

        expect(self.profile).to_have_text(message)

    def click_logout(self):

        self.logout.click()
