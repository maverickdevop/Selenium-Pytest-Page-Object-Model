import pytest
from tests.base_test import BaseTest
from config.config import TestData as Data


class TestSearch(BaseTest):

    def setUp(self):
        self.navigate_to_base_url()

    def test_search_input_visible(self):
        """ Check Search Form Exist """
        self.search_page.open_page(Data.BASE_URL)
        self.search_page.is_search_input_exists()

    def test_access_cookie(self):
        """ Accept Cookie """
        self.home_page.is_cookie_exists()
        self.home_page.accept_cookie()

    def test_search_page_title(self):
        """ Check Page Title With Search """
        self.search_page.check_page_title(Data.SEARCH_TITLE)

    def test_input_search_word(self):
        """ Search For Specific Word """
        self.search_page.do_search(Data.SEARCH_WORD)
        self.search_page.get_list_search_suggestion(Data.SEARCH_ASSERT)

    def test_check_product_cards(self):
        """ Click to see all products """
        self.search_page.check_product_list(Data.SEARCH_ASSERT)
        self.search_page.click_on_cards(Data.SEARCH_ASSERT)