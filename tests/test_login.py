import pytest
import os
from dotenv import load_dotenv
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
    Test a valid login scenario. Asserts that login is successful with correct credentials.
    Args:
        driver: Selenium WebDriver fixture.
    """
    if not HUDL_USERNAME or not HUDL_PASSWORD:
        pytest.skip(
            "HUDL_USERNAME and HUDL_PASSWORD must be set in the .env file."
        )
    page = LandingPage(driver)
    page.load()
    page.navigate_to_login()
    page = LoginPage(driver)
    page.load()
    page.enter_email(HUDL_USERNAME)
    page.click_continue_email()
    page.enter_password(HUDL_PASSWORD)
    page.click_continue_password()
    page = HomePage(driver)
    page.is_on_home_page()

#
# def test_invalid_login(driver):
#     """
#     Test an invalid login scenario. Asserts that an error message is shown for invalid credentials.
#     Args:
#         driver: Selenium WebDriver fixture.
#     """
#
#     page = LoginPage(driver)
#     page.load()
#     page.enter_email("invalid_email@domain.com")
#     page.enter_password("wrong_password")
#     page.submit()
#     assert "Invalid" in page.get_error_message()
#
#
# def test_missing_password(driver):
#     """
#     Test login with a missing password. Asserts that the appropriate error message is shown.
#     Args:
#         driver: Selenium WebDriver fixture.
#     """
#     if not HUDL_USERNAME:
#         pytest.skip("HUDL_USERNAME must be set in the .env file.")
#     page = LoginPage(driver)
#     page.load()
#     page.enter_email(HUDL_USERNAME)
#     page.enter_password("")
#     page.submit()
#     assert "Please enter your password" in page.get_error_message()
