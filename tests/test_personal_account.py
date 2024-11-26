import allure
from data import URLs


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет».')
    @allure.description('Предварительное создание и логирование пользователя; нажатина на кнопку «Личный кабинет»; '
                        'проверка корректности перехода на страницу профиля; удаление пользователя.')
    def test_cross_from_main_to_personal_account(self, cross_over, login_user):
        cross_over.go_to_profile_page()
        assert cross_over.get_current_url() == URLs.ACCOUNT_PROFILE_PAGE_URL

    @allure.title('Проверка перехода в раздел «История заказов».')
    @allure.description('Предварительное создание и логирование пользователя; переход на страницу профиля; '
                        'нажатие на кнопку "История заказов", поверка корректности открытия раздела истории; '
                        'удаление пользователя.')
    def test_cross_from_personal_account_to_order_history(self, cross_over, login_user, profile):
        cross_over.go_to_profile_page()
        profile.click_to_order_history_btn()
        assert profile.get_current_url() == URLs.ORDER_HISTORY_PAGE_URL

    @allure.title('Проверка возможности выхода из аккаунта.')
    @allure.description('Предварительное создание и логирование пользователя; переход на страницу профиля; '
                        'нажатие на кнопку "Выход", проверка перехода на страницу логирования; '
                        'удаление пользователя.')
    def test_logout_from_personal_account(self, cross_over, login_user, profile):
        cross_over.go_to_profile_page()
        profile.click_to_logout_btn()
        assert profile.get_current_url() == URLs.LOGIN_PAGE_URL
