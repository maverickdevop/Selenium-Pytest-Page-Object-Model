from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """ This class is the parent of all pages
    It contains all generic methods and utilities for all the pages"""

    def __init__(self, driver):
        """ Initial driver method """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def do_click(self, by_locator):
        """ Do click method to element """
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()
        return self

    def do_send_key(self, by_locator, text):
        """ Do send keys with keyword """
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        return self

    def get_element_text(self, by_locator):
        """ Get text in element """
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text, self

    def check_element_text(self, by_locator, text):
        """ Get text in element """
        element = self.wait.until(EC.visibility_of_element_located(by_locator)).text
        assert text in element, f"Expected text: {text} not located in {element}"

    def get_list_lenght(self, by_locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        return len(elements)

    def get_list_elements(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))

    def is_visible(self, by_locator):
        """ Visibility of element on page """
        self.wait.until(EC.visibility_of_element_located(by_locator))
        return self

    def elem_disappeared(self, by_locator):
        """ Check element is disappeared """
        self.wait.until(EC.invisibility_of_element(by_locator))
        return self

    def assert_title(self, title):
        """ Get page title """
        assert title in self.driver.title, f"Page have not expected title: {title}"

    def assert_text_in_list_elements(self, by_locator, text_expexted):
        """ Get list of elements """
        list_elems = []
        list_elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        for item in list_elements:
            list_elems.append(item.text)
        assert text_expexted in list_elems, f"Expected text: {text_expexted} not contains in list"
