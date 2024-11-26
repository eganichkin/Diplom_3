from selenium.webdriver.common.by import By


class ProfilePageLocators:
    SEARCH_ACCOUNT_NAME_INPUT = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[1]//input"
    SEARCH_ACCOUNT_EMAIL_INPUT = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[2]//input"
    SEARCH_ACCOUNT_PASSWORD_INPUT = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[3]//input"
    SEARCH_HISTORY_BTN = By.XPATH, "//a[text()='История заказов']"
    SEARCH_LOGOUT_BTN = By.XPATH, "//button[text()='Выход']"
    SEARCH_ORDER_HISTORY_LIST = By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]"

