from stepik_final_exam.pages.product_page import ProductPage
from stepik_final_exam.pages.base_page import BasePage
import time
import pytest


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     product_page = ProductPage(browser, link)
#     product_page.open() # откртыие страницы
#     product_page.add_to_basket()  # добавление товара
#     product_page.solve_quiz_and_get_code() # решение задачи в сплывающем окне
#     product_page.should_be_book_name() # проверка названия книги
#     product_page.should_be_book_price() # проверка цены книги

@pytest.mark.xfail(reason="")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() # откртыие страницы
    product_page.add_to_basket()  # добавление товара
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() # откртыие страницы
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() # откртыие страницы
    product_page.add_to_basket()  # добавление товара
    product_page.should_be_success_message()

# гость видит переход  на страницу логина с любой страницы 
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
# сам переход на страницу с логином
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
