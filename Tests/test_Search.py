import pytest
from Tests.test_base import BaseTest
from Pages.Search import SearchPage
from Pages.HomePage import HomePage
from Config.config import TestData
from Enums.global_enums import GlobalErrorMessages


class TestSearch(BaseTest):

    """ Check Search Form Exist """
    def test_search_input_visible(self):
        self.driver.get(TestData.BASE_URL)
        self.searchPage = SearchPage(self.driver)
        flag = self.searchPage.is_search_input_exists()
        assert flag, GlobalErrorMessages.WRONG_ELEMENT.value

    """ Accept Cookie """
    def test_access_cookie(self):
        self.searchPage = HomePage(self.driver)
        self.searchPage.is_cookie_exists()
        self.searchPage.accept_cookie()

    """ Check Page Title With Search """
    def test_search_page_title(self):
        self.searchPage = SearchPage(self.driver)
        title = self.searchPage.get_main_page_title()
        print("Website page title: ", title)
        assert TestData.SEARCH_TITLE in title, GlobalErrorMessages.WRONG_TITLE.value

    """ Search For Specific Word """
    def test_search(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.do_search(TestData.SEARCH_WORD)
        url = self.searchPage.get_page_url()
        assert TestData.BASE_URL in url, GlobalErrorMessages.WRONG_URL.value

    """ Search Word In Suggestion List"""
    def test_suggestion_word_list(self):
        self.searchPage = SearchPage(self.driver)
        words = self.searchPage.get_list_search_suggestion()

        for item in words:
            assert TestData.SEARCH_ASSERT in item, GlobalErrorMessages.WRONG_LIST.value

    """ Click to see all products """
    def test_click_all(self):
        self.searchPage = SearchPage(self.driver)
        h1 = self.searchPage.get_all_results()
        assert TestData.SEARCH_ASSERT in h1, GlobalErrorMessages.WRONG_TEXT.value

    """ Check all product cards for expected word """
    def test_check_product_card(self):
        self.searchPage = SearchPage(self.driver)
        list = self.searchPage.get_product_list()

        for item in list:
            assert TestData.SEARCH_ASSERT in item, GlobalErrorMessages.WRONG_LIST.value

    """ Click to all product cards """
    def test_click_cards(self):
        self.searchPage = SearchPage(self.driver)
        self.homePage = HomePage(self.driver)

        # Close sign-up pop-up window
        self.homePage.close_sign_up()

        # Click on each element in list
        title = self.searchPage.click_on_cards()
        assert TestData.SEARCH_ASSERT in title, GlobalErrorMessages.WRONG_LIST.value