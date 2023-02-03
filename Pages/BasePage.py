from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This class is the parent of all pages """
""" It contains all generic methods and utilities for all the pages"""


class BasePage:

    # Initial driver method
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.wait_long = WebDriverWait(self.driver, 120)

    # Do click method to element
    def do_click(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    # Do hover on element
    def do_hover(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    # Do send keys with keyword
    def do_send_key(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Get text in element
    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    # Visibility of element on page
    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # Get page title
    def get_title(self):
        return self.driver.title

    # Get page URL
    def get_url(self):
        return self.driver.current_url

    # Get list of elements
    def get_list_elements(self, by_locator):
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))