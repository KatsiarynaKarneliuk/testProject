from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators
from .pages.locators import MainPageLocators
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest      #для запуска именно этих тестов с меткой нужно добавить "-m login_guest"
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods_quantity()
    basket_page.should_be_text_about_empty_basket()

def test_link_has_substr(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page= LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_sould_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page= LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_form()


def test_sould_be_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page= LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_register_form()