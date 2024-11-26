import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators as Loc
from data import URLs, TEST_USER_EMAIL


class ForgotPasswordPage(BasePage):

    @allure.step('Переход на страницу восстановлени  пароля.')
    def open_forgot_password_page(self):
        self.open_page(URLs.FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Ввод почты для восстановления пароля; нажатие на кнопку "Восстановить; '
                 'ожидание закгрузки окна сброса пароля."')
    def input_email_for_recovery_password(self):
        self.send_text_to_element(Loc.SEARCH_EMAIL_RECOVERY, TEST_USER_EMAIL)
        self.click_to_element_by_script(Loc.SEARCH_BUTTON_RECOVERY)
        self.wait_for_redirect(URLs.RESET_PASSWORD_PAGE_URL)
