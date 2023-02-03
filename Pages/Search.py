import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Pages.HomePage
from Pages.BasePage import BasePage
from Config.config import TestData


class SearchPage(BasePage):

    """ Search Locators """
    SEARCH = (By.XPATH, "//input[@data-auto-id='searchinput-desktop']")
    SEARCH_DROPLIST = (By.XPATH, "//a[@data-auto-id='search-suggestion']/div[1]/span[1]")
    GET_ALL_LINK = (By.XPATH, "//div[@data-auto-id='search-results-container']/div/div[3]/a")
    H1_SEARCH_TITLE = (By.XPATH, "//h1[@data-auto-id='plp-header-bar-search-title']")
    PRODUCT_CARD_TITLE = (By.XPATH, "//p[@data-auto-id='product-card-title']")
    PRODUCT_HOCKEYCARD = (By.XPATH, "//div[@class='glass-product-card-container with-variation-carousel']")
    PRODUCT_TITLE = (By.XPATH, "(//h1[@data-auto-id='product-title']/span)[2]")

    """ Constructor Of The Page Class """

    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions For Search """
    def get_main_page_title(self):
        return self.get_title()

    """ Get page URL """
    def get_page_url(self):
        url = self.get_url()
        print("Page URL:", url)
        return url

    """ Check For Search Box Exist """
    def is_search_input_exists(self):
        return self.is_visible(self.SEARCH)

    """ Search For Sneakers """
    def do_search(self, search_word):
        self.do_click(self.SEARCH)
        self.do_send_key(self.SEARCH, search_word)

    """ Check Word Contains In List """
    def contain_in_list(self):
        return self.is_visible(self.SEARCH_DROPLIST)

    """ Get list of suggestion """
    def get_list_search_suggestion(self):
        word_list = self.get_list_elements(self.SEARCH_DROPLIST)
        words = []

        for i in word_list:
            words.append(i.text)

        print("List of suggestion words after search:", words)
        return words

    """ See all results and check title """
    def get_all_results(self):
        self.do_click(self.GET_ALL_LINK)
        h1 = self.get_element_text(self.H1_SEARCH_TITLE)
        print("Search title word:", h1)
        return h1

    """ Check product card list """
    def get_product_list(self):
        product_list = self.get_list_elements(self.PRODUCT_CARD_TITLE)
        products = []

        for i in product_list:
            products.append(i.text)

        print("List of products cards:", products)
        return products

    """ Click on all cards and check product """
    def click_on_cards(self):

        menu_elements = self.get_list_elements(self.PRODUCT_HOCKEYCARD)
        number_of_elements = len(menu_elements)

        for item in range(number_of_elements):
            menu_elements = self.get_list_elements(self.PRODUCT_HOCKEYCARD)
            link = menu_elements[item]
            link.click()

            title_card = self.get_element_text(self.PRODUCT_TITLE)
            return title_card

            driver.back()