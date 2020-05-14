
#from stepik_final_exam.pages.main_page import MainPage
from stepik_final_exam.pages.login_page import LoginPage
from stepik_final_exam.pages.product_page import ProductPage
from stepik_final_exam.pages.base_page import BasePage
from stepik_final_exam.pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    page2 = LoginPage(browser, link)
    page2.open()
    page2.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_enter_basket() #Переходит в корзину по кнопке в шапке 
    page2 = BasketPage(browser, browser.current_url)
    page2.is_basket_empty()
    page2.should_be_basket_empty()

