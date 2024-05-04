# Адреса endpoints
class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
    CREATE_USER_URL = BASE_URL + 'auth/register'
    LOGIN_USER_URL = BASE_URL + 'auth/login'
    DELETE_USER_URL = BASE_URL + 'auth/user'
    USER_EDIT_URL = BASE_URL + 'auth/user'
    CREATE_ORDER_URL = BASE_URL + 'orders'
    GET_ORDER_LIST_URL = BASE_URL + 'orders'
