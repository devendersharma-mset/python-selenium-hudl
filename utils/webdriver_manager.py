from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest
import os


def get_webdriver(browser_name: str):
    """
    Returns a Selenium WebDriver instance for the specified browser.

    Args:
        browser_name (str): The name of the browser ('chrome', 'firefox', 'edge').

    Returns:
        WebDriver: Selenium WebDriver instance for the specified browser.

    Raises:
        ValueError: If the browser is not supported.
    """
    browser_name = browser_name.lower()
    if browser_name == 'chrome':
        options = ChromeOptions()
        if os.getenv('HEADLESS', 'false').lower() == 'true':
            options.add_argument('--headless')
        return webdriver.Chrome(service=ChromeService(), options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        if os.getenv('HEADLESS', 'false').lower() == 'true':
            options.add_argument('--headless')
        return webdriver.Firefox(service=FirefoxService(), options=options)
    elif browser_name == 'edge':
        options = EdgeOptions()
        if os.getenv('HEADLESS', 'false').lower() == 'true':
            options.add_argument('--headless')
        return webdriver.Edge(service=EdgeService(), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


def pytest_addoption(parser):
    """
    Add a command-line option to pytest to specify the browser for tests.

    Args:
        parser: Pytest parser object.
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests: chrome, firefox, edge"
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Pytest fixture to provide a Selenium WebDriver instance based on the selected browser.

    Args:
        request: Pytest request object to access command-line options.

    Yields:
        WebDriver: Selenium WebDriver instance.
    """
    browser = request.config.getoption("--browser")
    driver = get_webdriver(browser)
    yield driver
    driver.quit() 