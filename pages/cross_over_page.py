import allure
from pages.base_page import BasePage
from locators.cross_over_locators import CrossOverLocators
from data import URLs


class CrossOverPage(BasePage):

    @allure.step('Переход на страницу заказов нажатиекм на кнопку "Лента заказов".')
    def go_to_feed_page(self):
        self.click_to_element_by_script(CrossOverLocators.SEARCH_ORDER_FEED_PAGE_LBL)

    @allure.step('Переход на основную страницу нажатием на кнопку "Конструктор".')
    def go_to_constructor_page(self):
        self.click_to_element_by_script(CrossOverLocators.SEARCH_CONSTRUCTOR_LBL)

    @allure.step('Переход на страницу профиля нажатием на кнопку "Личный кабинет".')
    def go_to_profile_page(self):
        self.click_to_element_by_script(CrossOverLocators.SEARCH_PERSONAL_ACCOUNT_LBL)
        self.wait_for_redirect(URLs.ACCOUNT_PROFILE_PAGE_URL)

