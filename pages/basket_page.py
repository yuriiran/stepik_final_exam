from stepik_final_exam.pages.base_page import BasePage
from stepik_final_exam.pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Item in basket"

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"
