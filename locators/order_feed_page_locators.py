from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    SEARCH_ORDER_ITEMS = By.XPATH, "//li [@class='OrderHistory_listItem__2x95r mb-6']"
    SEARCH_ORDER_ITEM = By.XPATH, "//li [@class='OrderHistory_listItem__2x95r mb-6'][1]"
    SEARCH_ORDER_COMPOSITION_LBL = By.XPATH, "//section[contains(@class ,'Modal_modal_opened')]"
    SEARCH_CLOSE_MODAL_WINDOW_BTN = By.XPATH, "//section[contains(@class ,'Modal_modal_opened')]//button"
    SEARCH_ORDER_ITEM_NUMBER = By.XPATH, "//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text " \
                                         "text_type_digits-default'] "
    SEARCH_ALL_TIME_COUNT_ORDER = By.XPATH, "//p [text() = 'Выполнено за все время:']/parent::*/p [contains(@class, " \
                                            "'OrderFeed_number__2MbrQ')] "
    SEARCH_TODAY_COUNT_ORDER = By.XPATH, "//p [text() = 'Выполнено за сегодня:']/parent::*/p [contains(@class, " \
                                         "'OrderFeed_number__2MbrQ')] "
    SEARCH_ORDER_NUMBERS_IN_WORK = By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]/li"
