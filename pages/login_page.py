from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in str(self.browser.driver.current_url), "не корректный url адрес login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина [id = "login_form"]
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "не форма логина"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице [id = "register_form"]
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "не форма логина"
