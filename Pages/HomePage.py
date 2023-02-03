from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData


class HomePage(BasePage):

    """ Search Locators """
    MODAL = (By.XPATH, "//div[@id='gl-modal__main-content-cookie-consent-modal']")
    ACCESS_MODAL = (By.XPATH, "//button[@id='glass-gdpr-default-consent-accept-button']")
    CLOSE_SIGNUP = (By.XPATH, "//button[@class='gl-modal__close']")

    """ Check For Modal Exist """
    def is_cookie_exists(self):
        return self.is_visible(self.MODAL)

    """ Accept Cookie """
    def accept_cookie(self):
        self.do_click(self.ACCESS_MODAL)

    """ Close Sign-Up Modal """
    def close_sign_up(self):
        self.do_click(self.CLOSE_SIGNUP)