import allure


class TestOrderFeed:

    @allure.title('Проверка, что если кликнуть на заказ, то откроется всплывающее окно с деталями.')
    @allure.description('Предварительное создание и логирование пользователя; переход на ленту заказов; '
                        'выбор и нажатие на заказ; проверка открытия окна с деталями; '
                        'удаление пользователя.')
    def test_click_order_feed_detail_is_open(self, login_user, cross_over, order_feed):
        cross_over.go_to_feed_page()
        order_feed.click_to_oder_feed_ingredient_item()
        assert order_feed.detail_modal_window_is_opened() is True

    @allure.title('Проверка, что заказы пользователя из «Истории заказов» отображаются на странице «Лента заказов».')
    @allure.description('Предварительное создание и логирование пользователя; создание нескольких заказов; '
                        'считывание списка номеров заказов из истории; считывание списка всех номеров из ленты;'
                        'проверка, что первый список является подсписком второго; удаление пользователя.')
    def test_display_orders_history_in_order_feed(self, user_methods, login_user, order_methods,
                                                  cross_over, order_feed, profile):
        order_count = 2
        order_methods.user_access_token = user_methods.get_user_access_token()
        order_methods.create_n_orders(order_count)

        cross_over.go_to_profile_page()
        order_history_list = profile.get_order_history_number_list(order_count)

        cross_over.go_to_feed_page()
        order_feed_list = order_feed.get_order_feed_number_list()
        assert set(order_history_list).issubset(order_feed_list)

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается.')
    @allure.description('Предварительное создание и логирование пользователя; считывание значения счётчика '
                        '"Выполнено за всё время" перед заказом; создание заказа; считывание значения счётчика '
                        'после выполнения заказа; проверка, что второе значение больше первого; удаление пользователя.')
    def test_create_order_counting_all_is_up(self, login_user, cross_over, order_feed, main):
        cross_over.go_to_feed_page()
        all_count_order_before = order_feed.get_all_count_order()
        cross_over.go_to_constructor_page()

        main.add_ingredient_to_order()
        main.create_order()
        main.close_details_window()

        cross_over.go_to_feed_page()
        all_count_order_after = order_feed.get_all_count_order()
        assert all_count_order_after > all_count_order_before

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается.')
    @allure.description('Предварительное создание и логирование пользователя; считывание значения счётчика '
                        '"Выполнено за сегодня" перед заказом; создание заказа; считывание значения счётчика '
                        'после выполнения заказа; проверка, что второе значение больше первого; удаление пользователя.')
    def test_create_order_counting_today_is_up(self, login_user, cross_over, order_feed, main):
        cross_over.go_to_feed_page()
        today_count_order_before = order_feed.get_today_count_order()

        cross_over.go_to_constructor_page()
        main.add_ingredient_and_create_order()
        main.close_details_window()

        cross_over.go_to_feed_page()
        today_count_order_after = order_feed.get_today_count_order()
        assert today_count_order_after > today_count_order_before

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе".')
    @allure.description('Предварительное создание и логирование пользователя; создание заказа; копирование номера '
                        'заказа из появившегося окна информации по заказу; переход в ленту заказов и проверка, '
                        'что данный номер содержится в разделе "В работе"; удаление пользователя.')
    def test_after_crate_detail_number_show_in_order_feed_work_status(self, login_user, cross_over, order_feed, main):
        main.add_ingredient_and_create_order()
        order_number_from_details = main.get_order_number_from_details_window()
        main.close_details_window()

        cross_over.go_to_feed_page()
        order_number_from_order_feed = order_feed.get_order_numbers_in_work()
        assert order_number_from_details in order_number_from_order_feed
