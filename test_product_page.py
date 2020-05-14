from stepik_final_exam.pages.product_page import ProductPage
from stepik_final_exam.pages.base_page import BasePage
from stepik_final_exam.pages.basket_page import BasketPage
from stepik_final_exam.pages.login_page import LoginPage
import time
import pytest
import faker
import random

f = faker.Faker()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() # откртыие страницы
    product_page.add_to_basket()  # добавление товара
    #product_page.solve_quiz_and_get_code() # решение задачи в сплывающем окне
    product_page.should_be_book_name() # проверка названия книги
    product_page.should_be_book_price() # проверка цены книги

@pytest.mark.xfail(reason="wrong message")
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

@pytest.mark.xfail(reason="isn't disappiring")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() # откртыие страницы
    product_page.add_to_basket()  # добавление товара
    product_page.should_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()

@pytest.mark.need_review       
# сам переход на страницу с логином
def test_guest_can_go_to_login_page_from_product_page (browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_enter_basket() #Переходит в корзину по кнопке в шапке 
    page2 = BasketPage(browser, browser.current_url)
    page2.is_basket_empty()
    page2.should_be_basket_empty()


#проверка для зарегистрированноого пользователя
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = f.email()
        password = str(time.time() + count)
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, link)
        self.product_page.open() # откртыие страницы
        self.product_page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, link)
        self.product_page.open() # откртыие страницы
        self.product_page.add_to_basket()  # добавление товара
        # self.product_page.solve_quiz_and_get_code() # решение задачи в сплывающем окне
        self.product_page.should_be_book_name() # проверка названия книги
        self.product_page.should_be_book_price() # проверка цены книги