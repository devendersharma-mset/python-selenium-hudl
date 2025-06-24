import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.config import HUDL_USERNAME, HUDL_PASSWORD


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and provide a headless Chrome WebDriver instance for tests.
    Yields:
        WebDriver: Selenium WebDriver instance.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Add this marker to re-run failed tests up to 2 times
def pytestmark():
    """
    Pytest marker to automatically rerun failed tests up to 2 times with a 1-second delay.
    """
    return pytest.mark.flaky(reruns=2, reruns_delay=1)


def test_valid_login(driver):
    """
    Test a valid login scenario. Asserts that login is successful with correct credentials.
    Args:
        driver: Selenium WebDriver fixture.
    """
    if not HUDL_USERNAME or not HUDL_PASSWORD:
        pytest.skip(
            "HUDL_USERNAME and HUDL_PASSWORD must be set as environment variables."
        )
    page = LoginPage(driver)
    page.load()
    page.enter_email(HUDL_USERNAME)
    page.enter_password(HUDL_PASSWORD)
    page.submit()
    assert page.is_login_successful()


def test_invalid_login(driver):
    """
    Test an invalid login scenario. Asserts that an error message is shown for invalid credentials.
    Args:
        driver: Selenium WebDriver fixture.
    """
    page = LoginPage(driver)
    page.load()
    page.enter_email("invalid_email@domain.com")
    page.enter_password("wrong_password")
    page.submit()
    assert "Invalid" in page.get_error_message()


def test_missing_password(driver):
    """
    Test login with a missing password. Asserts that the appropriate error message is shown.
    Args:
        driver: Selenium WebDriver fixture.
    """
    if not HUDL_USERNAME:
        pytest.skip("HUDL_USERNAME must be set as an environment variable.")
    page = LoginPage(driver)
    page.load()
    page.enter_email(HUDL_USERNAME)
    page.enter_password("")
    page.submit()
    assert "Please enter your password" in page.get_error_message()
