import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators as Loc


class OrderFeedPage(BasePage):

    @allure.step('Нажатие на элемент заказа в ленте.')
    def click_to_oder_feed_ingredient_item(self):
        self.click_to_element(Loc.SEARCH_ORDER_ITEM)

    @allure.step('Проверка открытия диалогового окна информации по заказу.')
    def detail_modal_window_is_opened(self):
        return self.element_is_available(Loc.SEARCH_CLOSE_MODAL_WINDOW_BTN)

    @allure.step('Получение списка номеров заказов из ленты заказов.')
    def get_order_feed_number_list(self):
        self.find_element_with_wait(Loc.SEARCH_ORDER_ITEMS)
        elements = self.find_all_elements_without_wait(Loc.SEARCH_ORDER_ITEMS)
        order_feed_list = []
        for element in elements:
            order_feed_list.append(element.text.split('\n')[0])
        return order_feed_list

    @allure.step('Получение количества заказов за всё время из ленты заказов.')
    def get_all_count_order(self):
        return self.get_text_from_element(Loc.SEARCH_ALL_TIME_COUNT_ORDER)

    @allure.step('Получение количества заказов за сегодня из ленты заказов.')
    def get_today_count_order(self):
        return self.get_text_from_element(Loc.SEARCH_TODAY_COUNT_ORDER)

    @allure.step('Получение списка номеров заказов из ленты заказов, находящихся в блоке "в работе".')
    def get_order_numbers_in_work(self):
        self.wait_before_text_change(Loc.SEARCH_ORDER_NUMBERS_IN_WORK, 'Все текущие заказы готовы!')
        elements = self.find_all_elements_without_wait(Loc.SEARCH_ORDER_NUMBERS_IN_WORK)
        order_numbers_in_work = []
        for element in elements:
            order_numbers_in_work.append(element.text)
        return order_numbers_in_work
