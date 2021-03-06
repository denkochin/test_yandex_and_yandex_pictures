from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        
    # Old version of the method without fancy locator
    """
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"
    """
    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"