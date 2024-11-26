import pytest
from selenium import webdriver
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from pages.cross_over_page import CrossOverPage
from pages.reset_password_page import ResetPasswordPage
from pages.forgot_password_page import ForgotPasswordPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def user_methods():
    return UserMethods()


@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture()
def user(user_methods):
    user_methods.post_create_user()
    yield
    user_methods.delete_user()


@pytest.fixture()
def login_user(driver, user_methods):
    user_methods.post_create_user()
    email, password = user_methods.get_email_password()
    login_page = LoginPage(driver, email, password)
    login_page.account_login()
    yield
    user_methods.delete_user()


@pytest.fixture()
def cross_over(driver):
    return CrossOverPage(driver)


@pytest.fixture()
def order_feed(driver):
    return OrderFeedPage(driver)


@pytest.fixture()
def main(driver):
    return MainPage(driver)


@pytest.fixture()
def profile(driver):
    return ProfilePage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def forgot_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture()
def reset_page(driver):
    return ResetPasswordPage(driver)
