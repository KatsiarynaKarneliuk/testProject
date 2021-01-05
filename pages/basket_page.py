from pages.base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def should_not_be_goods_quantity(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_QUANTITY), \
            'quantity of goods is  presented, but should not be'

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_FOR_EMPTY_CARD), \
            'text that basket is empty is not presented, but should  be'

