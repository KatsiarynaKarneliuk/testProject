from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "word \"login\" not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.

    def register_new_user(self,email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2)
        password_field2.send_keys(password)
        button =self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        button.click()
