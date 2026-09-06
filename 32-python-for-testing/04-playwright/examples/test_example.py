from playwright.sync_api import expect

def test_example(page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
