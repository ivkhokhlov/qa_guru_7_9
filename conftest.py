import pytest
from selene import browser


@pytest.fixture
def browser_settings():
    browser.config.driver_name = 'firefox'
