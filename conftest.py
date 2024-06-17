import pytest
from selene.support.shared import browser
from selene import have, be

@pytest.fixture()
def open_browser():
    browser.open('https://www.google.com/')
    browser.config.window_height = 1200
    browser.config.window_width = 1900