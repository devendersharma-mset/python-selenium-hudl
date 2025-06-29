from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIMEOUT)

    def wait_for_element(self, by, value, condition=EC.presence_of_element_located, timeout=None):
        """
        Wait for an element to satisfy a given condition.
        Args:
            by: Selenium By selector.
            value: The selector value.
            condition: The expected condition (default: presence_of_element_located).
            timeout: Optional timeout override.
        Returns:
            WebElement: The found element.
        """
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(condition((by, value))) 