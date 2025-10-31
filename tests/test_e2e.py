import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("op,expected", [
    ("add", "Result: 5"),
    ("subtract", "Result: -1"),
    ("multiply", "Result: 6"),
])
def test_calculator_ui(page: Page, op, expected):
    page.goto("http://127.0.0.1:8000/ui")
    page.fill("#a", "2")
    page.fill("#b", "3")
    page.select_option("#op", op)
    page.click("#calc")
    expect(page.locator("#result")).to_have_text(expected)

