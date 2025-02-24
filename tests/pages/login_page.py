from pages.base_pages import BasePage
from pages.locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    """Description """

    @allure.step("And user logs in to account")
    def login_to_account(self, login, password):
        self.find_element_and_send_key(LoginPageLocators.USERNAME_INPUT_FIELD, login)
        self.find_element_and_send_key(LoginPageLocators.PASSWORD_INPUT_FIELD, password)
        self.find_element_and_click(LoginPageLocators.SUBMIT_BUTTON)
