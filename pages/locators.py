from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner div.col-sm-6.product_main h1")
    PRODUCT_SUM = (By.CSS_SELECTOR, "#content_inner div.col-sm-6.product_main .price_color")
    MESSAGE_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    MESSAGE_SUM = (By.CSS_SELECTOR, "#messages .alert-info  p:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages div:nth-child(1) strong")