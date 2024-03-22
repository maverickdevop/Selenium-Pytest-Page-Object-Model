import pytest
from tests.test_base import BaseTest
from pages.search_page import SearchPage
from pages.home_page import HomePage
from config.config import TestData


class TestSearch(BaseTest):

    def test_search_input_visible(self):
        """ Check Search Form Exist """
        self.driver.get(TestData.BASE_URL)
        self.searchPage = SearchPage(self.driver)
        self.searchPage.is_search_input_exists()

    def test_access_cookie(self):
        """ Accept Cookie """
        self.searchPage = HomePage(self.driver)
        self.searchPage.is_cookie_exists()
        self.searchPage.accept_cookie()

    def test_search_page_title(self):
        """ Check Page Title With Search """
        self.searchPage = SearchPage(self.driver)
        self.searchPage.check_page_title(TestData.SEARCH_TITLE)

    def test_input_search_word(self):
        """ Search For Specific Word """
        self.searchPage = SearchPage(self.driver)
        self.searchPage.do_search(TestData.SEARCH_WORD)
        self.searchPage.get_list_search_suggestion(TestData.SEARCH_ASSERT)

    def test_check_product_cards(self):
        """ Click to see all products """
        self.searchPage = SearchPage(self.driver)
        self.searchPage.check_product_list(TestData.SEARCH_ASSERT)
        self.searchPage.click_on_cards(TestData.SEARCH_ASSERT)
