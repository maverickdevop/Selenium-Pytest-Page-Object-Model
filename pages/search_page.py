from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    """ Search Locators """
    SEARCH = (By.XPATH, "//input[@data-auto-id='searchinput-desktop']")
    SEARCH_DROPLIST = (By.XPATH, "//a[@data-auto-id='search-suggestion']//span")
    GET_ALL_LINK = (By.XPATH, "//div[@data-auto-id='search-results-container']/div/div[3]/a")
    H1_SEARCH_TITLE = (By.XPATH, "//h1[@data-auto-id='plp-header-bar-search-title']")
    PRODUCT_HOCKEYCARD = (By.XPATH, "//div[@data-auto-id='glass-product-card']")
    PRODUCT_TITLE = (By.XPATH, "(//h1[@data-auto-id='product-title']/span)[2]")

    def __init__(self, driver):
        """ Constructor Of The Page Class """
        super().__init__(driver)

    def check_page_title(self, title):
        """ Page Actions For Search """
        self.assert_title(title)

    def is_search_input_exists(self):
        """ Check For Search Box Exist """
        self.is_visible(self.SEARCH)

    def do_search(self, search_word):
        """ Search For Sneakers """
        self.do_click(self.SEARCH)
        self.do_send_key(self.SEARCH, search_word)

    def get_list_search_suggestion(self, text):
        """ Get list of suggestion """
        self.assert_text_in_list_elements(self.SEARCH_DROPLIST, text)

    def check_product_list(self, text):
        """ Check product card list """
        self.do_click(self.GET_ALL_LINK)
        self.check_element_text(self.H1_SEARCH_TITLE, text)

    def click_on_cards(self, text):
        """ Click on all cards and check product """
        number_of_elements = self.get_list_lenght(self.PRODUCT_HOCKEYCARD)
        for _ in range(number_of_elements):
            menu_elements = self.get_list_elements(self.PRODUCT_HOCKEYCARD)
            link = menu_elements[0]
            link.click()
            self.check_element_text(self.PRODUCT_TITLE, text)
            self.driver.back()
