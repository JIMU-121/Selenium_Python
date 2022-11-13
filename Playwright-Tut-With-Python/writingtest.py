import re
from playwright.sync_api import Page, expect, sync_playwright, Playwright


def test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = browser.context.new_page()





