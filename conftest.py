import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_settings():
    browser.config.driver_name = "chrome"
    browser.config.window_height = 1920
    browser.config.window_width = 1080

