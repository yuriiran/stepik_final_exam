from stepik_final_exam.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from stepik_final_exam.pages.locators import MainPageLocators
from stepik_final_exam.pages.login_page import LoginPage


class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
    #если добавляется алерт то необходимо прописать
        # alert = self.browser.switch_to.alert
        # alert.accept()
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        