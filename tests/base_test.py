import pytest
from pages.search_page import SearchPage
from pages.home_page import HomePage
from config.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    """ Page Factory for tests """
    home_page: HomePage
    search_page: SearchPage

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request, init_driver):
        """ Request list pf test Pages """
        request.cls.driver = init_driver
        request.cls.home_page = HomePage(init_driver)
        request.cls.search_page = SearchPage(init_driver)

    def navigate_to_base_url(self):
        """Navigate to base URL"""
        self.search_page.open_page(TestData.BASE_URL)