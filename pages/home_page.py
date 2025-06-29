from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    """
    Provides methods to interact with the Home page and validate successful login.
    """

    def verify_is_on_home_page(self):
        """
        Check if the Home page is loaded.
        """
        watchnow = self.wait_for_element(By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-watchnow']")
        assert watchnow is not None, "Watch Now nav element not found on home page."
        assert "home" in self.driver.current_url
