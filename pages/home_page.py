from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    """
    Page Object Model for the Hudl Home page.
    Provides methods to interact with the Home page.
    """

    def verify_is_on_home_page(self):
        home = self.wait_for_element(By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-home']")
        watchnow = self.wait_for_element(By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-watchnow']")
        upload = self.wait_for_element(By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-upload']")
        assert home is not None, "Home nav element not found on home page."
        assert watchnow is not None, "Watch Now nav element not found on home page."
        assert upload is not None, "Upload nav element not found on home page."
        assert "home" in self.driver.current_url
