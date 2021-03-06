from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_product_to_basket(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()


    def should_get_the_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME)
        message_name = message_name.text
        assert product_name == message_name, 'the name is different'

         
    def should_get_the_same_sum(self):
        product_sum = self.browser.find_element(*ProductPageLocators.PRODUCT_SUM)
        product_sum = product_sum.text
        message_sum = self.browser.find_element(*ProductPageLocators.MESSAGE_SUM)
        message_sum = message_sum.text
        assert product_sum == message_sum, 'the sum is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is not disappeared, but should be disappeared'
