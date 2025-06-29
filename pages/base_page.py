from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base class for all page objects. Provides common utilities for page interaction.
    """
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        """
        Initialize the BasePage with a Selenium WebDriver instance.
        Args:
            driver (WebDriver): The Selenium WebDriver instance to use.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIMEOUT)

    def wait_for_element(self, by, value, timeout=WAIT_TIMEOUT, condition=EC.visibility_of_element_located):
        """
        Wait for an element to be present and meet a given condition.
        Args:
            by (By): The type of selector to use (e.g., By.ID, By.CSS_SELECTOR).
            value (str): The selector value.
            timeout (int, optional): Maximum time to wait for the element. Defaults to 5 seconds.
            condition (callable, optional): The expected condition to wait for. Defaults to visibility_of_element_located.
        Returns:
            WebElement: The found web element.
        Raises:
            TimeoutException: If the element is not found within the timeout.
        """
        return WebDriverWait(self.driver, timeout).until(condition((by, value)))