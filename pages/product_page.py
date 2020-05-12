from stepik_final_exam.pages.base_page import BasePage
from stepik_final_exam.pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
    
    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert  book_price == basket_price, "Price is not same"

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_basket, "Name is not same"