from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        print(f"Launching {browser_type.name}...")
        browser = browser_type.launch(headless=False)  # Set to True if you want silent test
        page = browser.new_page()
        page.goto("https://example.com")
        print(f"{browser_type.name} title:", page.title())
        page.wait_for_timeout(2000)  # wait 2 seconds so you can visually confirm
        browser.close()
