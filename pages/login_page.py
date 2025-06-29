from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object Model for the Hudl login page.
    Provides methods to interact with the login form and validate login results.
    """
    URL = "https://www.hudl.com/login"
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        """
        Initialize the LoginPage with a Selenium WebDriver instance.
        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIMEOUT)

    def load(self):
        """
        Load the login page in the browser.
        """
        self.driver.get(self.URL)

    def wait_for_element_by_id(self, element_id):
        """
        Wait for an element to be present by its ID.
        Args:
            element_id (str): The ID of the element to wait for.
        Returns:
            WebElement: The found element.
        """
        return self.wait.until(EC.presence_of_element_located((By.ID, element_id)))

    def enter_email(self, email):
        """
        Enter the email address into the email input field.
        Args:
            email (str): The email address to enter.
        """
        self.wait_for_element_by_id("username").send_keys(email)

    def click_continue_email(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*=_button-login-id]"))).click()
    
    
    def enter_password(self, password):
        """
        Enter the password into the password input field.
        Args:
            password (str): The password to enter.
        """
        self.wait_for_element_by_id("password").send_keys(password)

    def click_continue_password(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*=_button-login-password]"))).click()

    def submit(self):
        """
        Click the login button to submit the form.
        """
        self.wait_for_element_by_id("logIn").click()

    def get_error_message(self):
        """
        Retrieve the error message displayed on failed login.
        Returns:
            str: The error message text.
        """
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-error-container")))
        return self.driver.find_element(By.CLASS_NAME, "login-error-container").text

    def is_login_successful(self):
        """
        Check if the login was successful by verifying the URL.
        Returns:
            bool: True if login is successful, False otherwise.
        """
        return "dashboard" in self.driver.current_url or "home" in self.driver.current_url

    def is_custom_logo_present(self):
        """
        Check if the custom logo div with id 'custom-prompt-logo' and title 'Hudl' is present, waiting up to WAIT_TIMEOUT seconds.
        Returns:
            bool: True if the element is found, False otherwise.
        """
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="custom-prompt-logo" and @title="Hudl"]')))
            return True
        except Exception:
            return False
