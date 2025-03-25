from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SEARCH_SHOW_HIDE_ICON = By.XPATH, "//div[@class='input__icon input__icon-action']//*[name()='svg']"
    SEARCH_INPUT_PASSWORD = By.XPATH, "//input[@name='Введите новый пароль']"
    SEARCH_ACTIVE_INPUT_STATUS_PASSWORD = By.XPATH, "//div[contains(@class,'status_active')]"
