from selenium.webdriver.common.by import By


class LoginPageLocators:
    SEARCH_LOGIN_EMAIL_INPUT = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[1]//input"
    SEARCH_LOGIN_PASSWORD_INPUT = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[2]//input"
    SEARCH_LOGIN_BTN = By.XPATH, "//button[text()='Войти']"
    SEARCH_REG_BTN = By.XPATH, "//а[text()='Зарегистрироваться']"
    SEARCH_RECOVERY_BTN = By.XPATH, "//a[text()='Восстановить пароль']"




