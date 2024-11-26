import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators as Loc


class ResetPasswordPage(BasePage):

    @allure.step('Нажатие по кнопке показать/скрыть пароль.')
    def click_to_show_hide_icon(self):
        self.click_to_element(Loc.SEARCH_SHOW_HIDE_ICON)

    @allure.step('Ввод тестового пароля.')
    def input_reset_password(self):
        self.send_text_to_element(Loc.SEARCH_INPUT_PASSWORD, 'TEST_PASSWORD')

    @allure.step('Проверка подсвечивания.')
    def input_status_password_is_active(self):
        if self.element_is_available(Loc.SEARCH_ACTIVE_INPUT_STATUS_PASSWORD):
            return True
        return False
