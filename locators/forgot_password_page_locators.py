from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    SEARCH_LABEL_RECOVERY = By.XPATH, "//h2[text() = 'Восстановление пароля']"
    SEARCH_EMAIL_RECOVERY = By.XPATH, "//input[@name = 'name']"
    SEARCH_BUTTON_RECOVERY = By.XPATH, "//button[text() = 'Восстановить']"
