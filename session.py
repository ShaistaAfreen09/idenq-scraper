import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hiring.idenhq.com/")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("wYjlGsU6")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("sneha.hosamani@cmr.edu.in")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Launch Challenge").click()
    page.get_by_role("button", name="Dashboard Tools").click()
    page.get_by_role("button", name="Open Data Visualization").click()
    page.get_by_role("button", name="Data Visualization").click()
    page.get_by_role("button", name="Open Inventory Management").click()
    page.get_by_role("button", name="Inventory Management").click()
    page.get_by_role("button", name="View Product Inventory").click()
    page.get_by_role("region", name="Inventory Management").locator("div").nth(1).click()
    page.get_by_role("button", name="View Product Inventory").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.locator("div").filter(has_text=re.compile(r"^ID:154Cost\$51\.90ManufacturerValueCreatorsModified2025-03-22$")).first.click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()
    page.get_by_text("Innovative Beauty UltraID:0Cost$895.49ManufacturerTechCorpModified2025-02-23Eco").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
