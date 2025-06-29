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
        self.driver.get(self.URL)

    def enter_email(self, email):
        self.wait_for_element(By.ID, "username").send_keys(email)

    def click_continue_email(self):
        self.wait_for_element(By.CSS_SELECTOR, "[class*=_button-login-id]", condition=EC.presence_of_element_located).click()

    def enter_password(self, password):
        self.wait_for_element(By.ID, "password").send_keys(password)

    def click_continue_password(self):
        self.wait_for_element(By.CSS_SELECTOR, "[class*=_button-login-password]", condition=EC.presence_of_element_located).click()

    def submit(self):
        self.wait_for_element(By.ID, "logIn").click()

    def get_username_error_message(self):
        error_element = self.wait_for_element(By.ID, "error-element-username", timeout=10)
        actual_error_message = error_element.text
        print(f"actual error message: {actual_error_message}")
        return actual_error_message

    def get_password_error_message(self):
        error_element = self.wait_for_element(By.ID, "error-element-password", timeout=10)
        actual_error_message = error_element.text
        print(f"actual error message: {actual_error_message}")
        return actual_error_message