from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LandingPage(BasePage):
    """
    Page Object Model for the Hudl Landing page.
    Provides methods to interact with the Landing page.
    """

    URL = "https://www.hudl.com/en_gb/"

    def load(self):
        """
        Load the Landing page in the browser.
        """
        self.driver.get(self.URL)

    def navigate_to_login(self):
        """
        Navigate to the login page by clicking the login selectors, waiting for each element.
        """
        self.wait_for_element(By.CSS_SELECTOR, "[data-qa-id='login-select']", condition=EC.element_to_be_clickable).click()
        self.wait_for_element(By.CSS_SELECTOR, "[data-qa-id='login-hudl']", condition=EC.element_to_be_clickable).click()
        self.wait_for_element(By.XPATH, '//div[@id="custom-prompt-logo" and @title="Hudl"]')
