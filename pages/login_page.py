import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as LoginLoc
from locators.main_page_locators import MainPageLocators as MainLoc
from data import URLs


class LoginPage(BasePage):

    def __init__(self, driver, email='', password=''):
        super().__init__(driver)
        self.user_email = email
        self.user_password = password

    @allure.step('Открытие окна логирования.')
    def open_login_page(self):
        self.open_page(URLs.LOGIN_PAGE_URL)

    @allure.step('Нажатие на кнопку "Восстановить пароль".')
    def click_to_recovery_btn(self):
        self.click_to_element_by_script(LoginLoc.SEARCH_RECOVERY_BTN)

    @allure.step('Ввод логина и пароля, нажатие на кнопку "Войти".')
    def account_login(self):
        self.open_login_page()
        self.send_text_to_element(LoginLoc.SEARCH_LOGIN_EMAIL_INPUT, self.user_email)
        self.send_text_to_element(LoginLoc.SEARCH_LOGIN_PASSWORD_INPUT, self.user_password)
        self.click_to_element_by_script(LoginLoc.SEARCH_LOGIN_BTN)
        self.find_element_with_wait(MainLoc.SEARCH_DRAG_BUN_UP)

