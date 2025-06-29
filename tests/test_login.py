import pytest
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage


# Load environment variables from .env file
load_dotenv()

# Load credentials from environment variables (via .env file)
HUDL_USERNAME = os.getenv("HUDL_USERNAME")
HUDL_PASSWORD = os.getenv("HUDL_PASSWORD")

def test_valid_login(driver):
    """
    Test a valid login scenario:
    - Loads the landing page
    - Navigates to the login page
    - Enters valid credentials
    - Verifies successful navigation to the home page
    """
    if not HUDL_USERNAME or not HUDL_PASSWORD:
        pytest.skip("HUDL_USERNAME and HUDL_PASSWORD must be set in the .env file.")

    landing = LandingPage(driver)
    landing.load()
    landing.navigate_to_login()

    login = LoginPage(driver)
    login.enter_email(HUDL_USERNAME)
    login.click_continue_email()
    login.enter_password(HUDL_PASSWORD)
    login.click_continue_password()

    # Wait for the URL to contain 'home' after login
    home = HomePage(driver)
    home.verify_is_on_home_page()


def test_invalid_email_format(driver):
    """
    Test login with an invalid email format:
    - Loads the landing page
    - Navigates to the login page
    - Enters an invalid email format
    - Verifies the correct error message is displayed for the username field
    """
    landing = LandingPage(driver)
    landing.load()
    landing.navigate_to_login()

    login = LoginPage(driver)
    login.enter_email("invalid_email")
    login.click_continue_email()
    assert "Enter a valid email." in login.get_username_error_message()

def test_invalid_username_or_password(driver):
    """
    Test login with invalid username or password:
    - Loads the landing page
    - Navigates to the login page
    - Enters an invalid email and password
    - Verifies the correct error message is displayed for the password field
    """
    landing = LandingPage(driver)
    landing.load()
    landing.navigate_to_login()

    login = LoginPage(driver)
    login.enter_email("invalid_email@gmail.com")
    login.click_continue_email()
    login.enter_password('abc123456!')
    login.click_continue_password()

    assert "Incorrect username or password." in login.get_password_error_message()
