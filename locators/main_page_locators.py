from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_BUNS_INGREDIENT_ITEM = By.XPATH, "//img[@alt = 'Краторная булка N-200i']"
    SEARCH_BUNS_COUNTER_INGREDIENT_ITEM = By.XPATH, "//img[@alt = 'Краторная булка N-200i']/parent::*//p[" \
                                                    "@class='counter_counter__num__3nue1'] "
    SEARCH_SAUCES_ITEM = By.XPATH, "//img[@alt =  'Соус Spicy-X']"
    SEARCH_INGREDIENT_DETAIL = By.XPATH, "//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
    SEARCH_DRAG_BUN_UP = By.XPATH, "//span[text() = 'Перетяните булочку сюда (верх)']"
    SEARCH_CREATE_ORDER_BTN = By.XPATH, "//button[text() = 'Оформить заказ']"
    SEARCH_ORDER_HAS_STARTED = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]"
    SEARCH_CLOSE_INGREDIENT_DETAIL_BTN = By.XPATH, "//button[contains(@class,'close')]"
    SEARCH_ORDER_NUMBER_FROM_DETAILS_WINDOW = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]"
