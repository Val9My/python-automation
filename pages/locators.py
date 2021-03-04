from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    #USER_ICON = (By.CSS_SELECTOR, ".alert-success .alertinner.wicon")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.ID, "id_login-username")
    PASSWORD_INPUT = (By.ID, "id_login-password")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONF_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.ID, "content_inner")
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

