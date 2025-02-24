import allure
from pages.base_pages import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    """Description """

    @allure.step("And user proceeds to login page")
    def navigate_to_login_page(self):
        self.find_element_and_click(HomePageLocators.LOGIN_LINK)

    @allure.step("And user see logout link")
    def is_logout_link_visible(self):
        return self.find_element(HomePageLocators.LOGOUT_LINK)

    @allure.step("And user selects movie")
    def select_movie(self, name):
        self.find_element_and_send_key(HomePageLocators.SEARCH_INPUT_FIELD, name)
        self.find_element_and_click(HomePageLocators.SEARCH_BUTTON)
        self.find_element_and_click(HomePageLocators.MOVIE_ITEM)

    @allure.step("And user rates movie")
    def rate_movie(self):
        self.find_element_and_click(HomePageLocators.RATE_SIGN)
        self.find_element_and_click(HomePageLocators.SUBMIT_BUTTON)

    @allure.step("And user see success label text")
    def is_movie_rated(self):
        return self.find_element(HomePageLocators.RATE_ACCEPTED_TEXT)
