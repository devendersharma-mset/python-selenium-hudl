from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    """
    Page Object Model for the Hudl Landing page.
    Provides methods to interact with the Landing page.
    """

    URL = "https://www.hudl.com/en_gb/"
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        """
        Initialize the LandingPage with a Selenium WebDriver instance.
        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIMEOUT)

    def load(self):
        """
        Load the Landing page in the browser.
        """
        self.driver.get(self.URL)

    def navigate_to_login(self):
        """
        Navigate to the login page by clicking the login selectors, waiting for each element.
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa-id='login-select']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa-id='login-hudl']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="custom-prompt-logo" and @title="Hudl"]')))
