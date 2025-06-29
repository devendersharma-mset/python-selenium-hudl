import pytest
from utils.webdriver_manager import get_webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests: chrome, firefox, edge"
    )


@pytest.fixture
def driver(request):
    """
    Pytest fixture to provide a Selenium WebDriver instance based on the selected browser.
    Yields:
        WebDriver: Selenium WebDriver instance.
    """
    browser = request.config.getoption("--browser")
    driver = get_webdriver(browser)
    yield driver
    driver.quit() 