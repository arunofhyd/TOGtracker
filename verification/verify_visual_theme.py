import os
from playwright.sync_api import sync_playwright

def verify_visual_theme():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        page.goto(f"file://{os.getcwd()}/index.html")

        # Click Guest
        page.click("#offline-btn")
        page.wait_for_timeout(1000)

        # 1. Screenshot Light Mode (Moon should be visible)
        page.screenshot(path="verification/header_light.png")
        print("Captured Light Mode (Moon visible)")

        # Toggle Dark Mode
        page.click("button[onclick='toggleTheme()']")
        page.wait_for_timeout(500)

        # 2. Screenshot Dark Mode (Sun should be visible)
        page.screenshot(path="verification/header_dark.png")
        print("Captured Dark Mode (Sun visible)")

        browser.close()

if __name__ == "__main__":
    verify_visual_theme()
