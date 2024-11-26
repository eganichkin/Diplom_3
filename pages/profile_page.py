import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators as Loc
from data import URLs


class ProfilePage(BasePage):

    @allure.step('Нажатие на кнопку "История заказов", ожидание закгрузки страницы истории.')
    def click_to_order_history_btn(self):
        self.click_to_element_by_script(Loc.SEARCH_HISTORY_BTN)
        self.wait_for_redirect(URLs.ORDER_HISTORY_PAGE_URL)

    @allure.step('Нажатие на кнопку "Выход", ожидание закгрузки страницы логирования.')
    def click_to_logout_btn(self):
        self.click_to_element_by_script(Loc.SEARCH_LOGOUT_BTN)
        self.wait_for_redirect(URLs.LOGIN_PAGE_URL)

    @allure.step('Получение списка с номерами заказов из "Истории заказов" в количестве N штук.')
    def get_order_history_number_list(self, n):
        self.click_to_order_history_btn()
        elements = self.find_all_elements_with_wait(Loc.SEARCH_ORDER_HISTORY_LIST, n)
        order_history_list = []
        for element in elements:
            order_history_list.append(element.text.split('\n')[0])
        return order_history_list
