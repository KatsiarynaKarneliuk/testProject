from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators
from pages.locators import MainPageLocators
from pages.base_page import BasePage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина

def test_link_has_substr():
    link = "http://selenium1py.pythonanywhere.com/"
    page= LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_sould_be_login_form():
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    page.should_be_login_form()


def test_sould_be_registration_form():
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    page.should_be_register_form()