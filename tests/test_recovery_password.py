import allure
from data import URLs


class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль».')
    @allure.description('Переход на страницу логирования; нажатие на кнопку "Восстановить пароль"; '
                        'проверка перехода на страницу восстановления пароля".')
    def test_cross_from_login_page_to_forgot_password_page(self, login_page):
        login_page.open_login_page()
        login_page.click_to_recovery_btn()
        assert login_page.get_current_url() == URLs.FORGOT_PASSWORD_PAGE_URL

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить».')
    @allure.description('Переход на страницу восстановления пароля; ввод почты; нажатие на кнопку "Восстановить";'
                        'проверка перехода на страницу сброса пароля".')
    def test_cross_from_forgot_password_page_to_reset_password_page(self, forgot_page):
        forgot_page.open_forgot_password_page()
        forgot_page.input_email_for_recovery_password()
        assert forgot_page.get_current_url() == URLs.RESET_PASSWORD_PAGE_URL

    @allure.title('Проверка клика по кнопке показать/скрыть пароль, активации его подсвечивания.')
    @allure.description('Переход в окно восстановления пароля; ввод пароля; проверка, что по кнопке показать/скрыть '
                        'происходит подсвечивание поля ввода.')
    def test_click_to_show_hide_icon(self, forgot_page, reset_page):
        forgot_page.open_forgot_password_page()
        forgot_page.input_email_for_recovery_password()
        reset_page.click_to_show_hide_icon()
        reset_page.input_reset_password()
        assert reset_page.input_status_password_is_active()
