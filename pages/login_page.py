from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object Model for the Hudl login page.
    Provides methods to interact with the login form and validate login results.
    """

    URL = "https://www.hudl.com/login"

    def __init__(self, driver):
        """
        Initialize the LoginPage with a Selenium WebDriver instance.
        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver

    def load(self):
        """
        Load the login page in the browser.
        """
        self.driver.get(self.URL)

    def enter_email(self, email):
        """
        Enter the email address into the email input field.
        Args:
            email (str): The email address to enter.
        """
        self.driver.find_element(By.ID, "email").send_keys(email)

    def enter_password(self, password):
        """
        Enter the password into the password input field.
        Args:
            password (str): The password to enter.
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def submit(self):
        """
        Click the login button to submit the form.
        """
        self.driver.find_element(By.ID, "logIn").click()

    def get_error_message(self):
        """
        Retrieve the error message displayed on failed login.
        Returns:
            str: The error message text.
        """
        return self.driver.find_element(By.CLASS_NAME, "login-error-container").text

    def is_login_successful(self):
        """
        Check if the login was successful by verifying the URL.
        Returns:
            bool: True if login is successful, False otherwise.
        """
        return (
            "dashboard" in self.driver.current_url or "home" in self.driver.current_url
        )
