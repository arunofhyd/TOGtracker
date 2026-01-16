import os
from playwright.sync_api import sync_playwright

def verify_visual():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        page.goto(f"file://{os.getcwd()}/index.html")

        # Click "Continue as Guest"
        page.click("#offline-btn")

        # Wait for app
        page.wait_for_selector("#app-container")

        # Screenshot 1: Guest Header with SVG Avatar
        page.screenshot(path="verification/guest_header.png")
        print("Screenshot saved: verification/guest_header.png")

        # Open Dropdown
        page.click("#user-avatar-btn")
        page.wait_for_timeout(500) # Wait for animation

        # Screenshot 2: Dropdown Open
        page.screenshot(path="verification/guest_dropdown.png")
        print("Screenshot saved: verification/guest_dropdown.png")

        browser.close()

if __name__ == "__main__":
    verify_visual()
