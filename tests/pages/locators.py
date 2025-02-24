from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for Start page locators. All Start page locators should come here"""
    USERNAME_INPUT_FIELD = (By.ID, "id_username")
    PASSWORD_INPUT_FIELD = (By.ID, "id_password")
    SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class,'btn btn-success')]")


class HomePageLocators(object):
    """A class for Start page locators. All Start page locators should come here"""
    LOGIN_LINK = (By.XPATH, "//*[contains(@href,'/login/')]")
    LOGOUT_LINK = (By.XPATH, "//*[contains(@href,'/logout/')]")
    SEARCH_INPUT_FIELD = (By.XPATH, "//input[contains(@class,'form-control input-lg')]")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'btn btn-info btn-lg')]")
    MOVIE_ITEM = (By.XPATH, "//*[contains(@href, '/146/')]")
    RATE_SIGN = (By.XPATH, "//*[contains(@data-rating,'4')]")
    SUBMIT_BUTTON = (By.XPATH, "//*[contains(@type,'submit')]")
    RATE_ACCEPTED_TEXT = (By.XPATH, "//*[contains(@class,'success')]")
