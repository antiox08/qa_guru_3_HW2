import pytest
from selene.support.shared import browser
from selene import have, be

def test_google_search(open_browser):
    browser.element('[name="q"]').should(be.blank).press_enter().type('selene').press_enter()
    browser.element('#search').should(have.texts('yashaka/selene: User-oriented Web UI browser tests in'))

def test_google_search_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).press_enter().type('addfaswqef2q3f232f3f').press_enter()
    browser.element('#search').should(have.texts('По запросу addfaswqef2q3f232f3f ничего не найдено. '))