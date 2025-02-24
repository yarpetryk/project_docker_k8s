import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from helpers.config_env import config_env

import time


class TestMovieList:
    # Setting up the initialization
    def init(self, web_driver):
        self.driver = web_driver
        self.driver.delete_all_cookies()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.login = config_env().get('login')
        self.password = config_env().get('password')

    @pytest.mark.smoke
    def test_movie_list(self, web_driver):

        # Initialization
        self.init(web_driver)

        # Proceed to Login page
        self.home_page.navigate_to_login_page()

        # Login to account
        self.login_page.login_to_account(self.login, self.password)

        # Assert Logout button
        assert self.home_page.is_logout_link_visible()

        # Select movie
        self.home_page.select_movie('Casper')

        # Rate movie
        self.home_page.rate_movie()

        # Assert movie is rated
        assert self.home_page.is_movie_rated()
