import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Loc
from data import URLs


class MainPage(BasePage):

    @allure.step('Открытие основной страницы.')
    def open_main_page(self):
        self.open_page(URLs.BASE_URL)

    @allure.step('Клик по записи ингредиента.')
    def click_to_ingredient(self):
        self.click_to_element_by_script(Loc.SEARCH_BUNS_INGREDIENT_ITEM)

    @allure.step('Проверка открытия окна с деталями по ингредиенту.')
    def ingredient_detail_is_active(self):
        return self.element_is_available(Loc.SEARCH_INGREDIENT_DETAIL)

    @allure.step('Нажатие на "крестик" окна с деталями по ингредиенту.')
    def close_details_window(self):
        self.click_to_element_by_script(Loc.SEARCH_CLOSE_INGREDIENT_DETAIL_BTN)

    @allure.step('Ожидание доступности элемента конструктора, перетаскивание элемента ингридиента к заказу.')
    def add_ingredient_to_order(self):
        self.find_element_with_wait(Loc.SEARCH_DRAG_BUN_UP)
        self.drag_and_drop_element(Loc.SEARCH_BUNS_INGREDIENT_ITEM, Loc.SEARCH_DRAG_BUN_UP)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def create_order(self):
        self.click_to_element(Loc.SEARCH_CREATE_ORDER_BTN)

    @allure.step('Добавление ингридиента в заказ, создание заказа.')
    def add_ingredient_and_create_order(self):
        self.add_ingredient_to_order()
        self.create_order()

    @allure.step('Считывание значения каунтера ингредиента.')
    def get_counter(self):
        return self.get_text_from_element(Loc.SEARCH_BUNS_COUNTER_INGREDIENT_ITEM)

    @allure.step('Признак создания заказа.')
    def order_is_created(self):
        return self.element_is_available(Loc.SEARCH_ORDER_HAS_STARTED)

    @allure.step('Считывание номера заказа из окна деталей по заказу.')
    def get_order_number_from_details_window(self):
        self.wait_before_text_change(Loc.SEARCH_ORDER_NUMBER_FROM_DETAILS_WINDOW, '9999')
        return '0' + self.get_text_from_element(Loc.SEARCH_ORDER_NUMBER_FROM_DETAILS_WINDOW)
