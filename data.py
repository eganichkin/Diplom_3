class URLs:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    AUTH_URL = BASE_URL + 'api/auth'
    USER_URL = BASE_URL + 'api/auth/user'
    LOGIN_URL = BASE_URL + 'api/auth/login'
    REGISTER_URL = BASE_URL + 'api/auth/register'
    ORDERS_URL = BASE_URL + 'api/orders'

    LOGIN_PAGE_URL = BASE_URL + 'login'
    FORGOT_PASSWORD_PAGE_URL = BASE_URL + 'forgot-password'
    RESET_PASSWORD_PAGE_URL = BASE_URL + 'reset-password'
    ACCOUNT_PAGE_URL = BASE_URL + 'account/'
    ACCOUNT_PROFILE_PAGE_URL = ACCOUNT_PAGE_URL + 'profile'
    ORDER_HISTORY_PAGE_URL = BASE_URL + 'account/order-history'
    ORDER_FEED_PAGE_URL = BASE_URL + 'feed'


TEST_USER_EMAIL = 'test_email@yandex.ru'
DEFAULT_WAIT_TIME = 10

ORDER_INFO = {
    "ingredients": [
        "61c0c5a71d1f82001bdaaa73",
        "61c0c5a71d1f82001bdaaa75",
        "61c0c5a71d1f82001bdaaa6c"
    ]
}
