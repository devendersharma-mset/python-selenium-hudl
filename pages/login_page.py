from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    """
    Page Object Model for the Hudl login page.
    Provides methods to interact with the login form and validate login results.
    """
    URL = "https://www.hudl.com/login"

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
        self.wait_for_element(By.ID, "username").send_keys(email)

    def click_continue_email(self):
        """
        Click the continue button after entering the email.
        """
        self.wait_for_element(By.CSS_SELECTOR, "[class*=_button-login-id]", condition=EC.presence_of_element_located).click()

    def enter_password(self, password):
        """
        Enter the password into the password input field.
        Args:
            password (str): The password to enter.
        """
        self.wait_for_element(By.ID, "password").send_keys(password)

    def click_continue_password(self):
        """
        Click the continue button after entering the password.
        """
        self.wait_for_element(By.CSS_SELECTOR, "[class*=_button-login-password]", condition=EC.presence_of_element_located).click()

    def submit(self):
        """
        Click the login button to submit the form.
        """
        self.wait_for_element(By.ID, "logIn").click()

    def get_username_error_message(self):
        """
        Wait for and return the username error message text.
        Returns:
            str: The error message text for the username field.
        """
        error_element = self.wait_for_element(By.ID, "error-element-username", timeout=10)
        actual_error_message = error_element.text
        print(f"actual error message: {actual_error_message}")
        return actual_error_message

    def get_password_error_message(self):
        """
        Wait for and return the password error message text.
        Returns:
            str: The error message text for the password field.
        """
        error_element = self.wait_for_element(By.ID, "error-element-password", timeout=10)
        actual_error_message = error_element.text
        print(f"actual error message: {actual_error_message}")
        return actual_error_message