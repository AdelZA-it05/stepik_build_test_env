from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from .login_page import LoginPage
from .base_page import BasePage

class MainPage(BasePage):
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login link")
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
