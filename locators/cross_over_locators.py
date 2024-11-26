from selenium.webdriver.common.by import By


class CrossOverLocators:
    SEARCH_ORDER_FEED_PAGE_LBL = By.XPATH, "//p[text() = 'Лента Заказов']"
    SEARCH_CONSTRUCTOR_LBL = By.XPATH, "//p[text() = 'Конструктор' ]"
    SEARCH_PERSONAL_ACCOUNT_LBL = By.XPATH, "//p[text() = 'Личный Кабинет']"

