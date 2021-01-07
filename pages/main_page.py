from .base_page import basepage
class MainPage(basepage):
    def go_to_login_page(self):
        login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element_by_css_selector("#login_link")
