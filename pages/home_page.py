from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """
    Page Object Model for the Hudl Home page.
    Provides methods to interact with the Home page.
    """
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        """
        Initialize the LandingPage with a Selenium WebDriver instance.
        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIMEOUT)

    def is_on_home_page(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-home']")))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-watchnow']")))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-upload']")))
