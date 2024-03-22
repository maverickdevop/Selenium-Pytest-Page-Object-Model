from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """ Search Locators """
    MODAL = (By.XPATH, "//div[@id='gl-modal__main-content-']")
    ACCESS_MODAL = (By.XPATH, "//button[@id='glass-gdpr-default-consent-accept-button']")

    def is_cookie_exists(self):
        """ Check For Modal Exist """
        self.is_visible(self.MODAL)

    def accept_cookie(self):
        """ Accept Cookie """
        self.do_click(self.ACCESS_MODAL)
        self.elem_disappeared(self.MODAL)
