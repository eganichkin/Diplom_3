import allure
from data import URLs


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Конструктор».')
    @allure.description('Предварительное создание и логирование пользователя; переход на страницу профиля; '
                        'нажатие на кнопку "Конструктор"; проверка загрузки основной страницы сайта; '
                        'удаление пользователя.')
    def test_cross_from_personal_account_to_main(self, cross_over, login_user):
        cross_over.go_to_profile_page()
        cross_over.go_to_constructor_page()
        assert cross_over.get_current_url() == URLs.BASE_URL

    @allure.title('Проверка перехода по клику на страницу «Лента заказов».')
    @allure.description('Предварительное создание и логирование пользователя; нажатие на кнопку "Лента заказов"; '
                        'проверка корректности перехода; удаление пользователя.')
    def test_cross_from_main_to_order_feed(self, cross_over, login_user):
        cross_over.go_to_feed_page()
        assert cross_over.get_current_url() == URLs.ORDER_FEED_PAGE_URL

    @allure.title('Проверка появивления всплывающего окна с деталями при клике на ингредиент.')
    @allure.description('Предварительное создание и логирование пользователя; нажатие на элементе ингредиента; '
                        'проверка появивления всплывающего окна с информацией по ингридиенту; удаление пользователя.')
    def test_click_to_ingredient_show_ingredient_details_window(self, main, login_user):
        main.click_to_ingredient()
        assert main.ingredient_detail_is_active() is True

    @allure.title('Проверка, что всплывающее окно закрывается кликом по крестику.')
    @allure.description('Предварительное создание и логирование пользователя; нажатие по инредиенту, '
                        'переход к информацией по ингридиенту, нажтие на крестик, '
                        'проверка корректности закрытия диалогового окна; удаление пользователя.')
    def test_close_ingredient_details_window(self, main, login_user):
        main.click_to_ingredient()
        main.close_details_window()
        assert main.ingredient_detail_is_active() is False

    @allure.title('Проверка, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента.')
    @allure.description('Предварительное создание и логирование пользователя; считывание первоночального значения '
                        'каунтера ингредиента; добавление ингридента к заказу, создание заказа; '
                        'повторное считываение каунтера, проверка, что его значение стало > первоначального;'
                        'удаление пользователя.')
    def test_add_ingredient_counter_increment_is_up(self, main, login_user):
        counter_before_add = main.get_counter()
        main.add_ingredient_to_order()
        counter_after_add = main.get_counter()
        assert counter_after_add > counter_before_add

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ.')
    @allure.description('Предварительное создание и логирование пользователя; добавление ингридента к заказу, '
                        'создание заказа; проверка появления информации с подтверждение создания в диалоговом окне;'
                        'удаление пользователя.')
    def test_login_user_can_create_order(self, main, login_user):
        main.add_ingredient_to_order()
        main.create_order()
        assert main.order_is_created() is True
