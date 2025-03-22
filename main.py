import json
from playwright.sync_api import Playwright, sync_playwright

def extract_product_data(page):
   
    product_cards = page.locator("div:has-text('ID: ')") 
    data = []

    for i in range(product_cards.count()):
        card = product_cards.nth(i)
        product_info = {
            "ID": card.locator("text=ID:").nth(0).inner_text().split(":")[-1].strip(),
            "Name": card.locator("h5").inner_text(),
            "Cost": card.locator("text=Cost").nth(0).inner_text().split(":")[-1].strip(),
            "Manufacturer": card.locator("text=Manufacturer").nth(0).inner_text().split(":")[-1].strip(),
            "Modified": card.locator("text=Modified").nth(0).inner_text().split(":")[-1].strip(),
        }
        data.append(product_info)

    return data

def save_to_json(data, filename="product_inventory.json"):
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    
    page.goto("https://hiring.idenhq.com/")
    page.get_by_role("textbox", name="Password").fill("wbrdx6n0")
    page.get_by_role("textbox", name="Email").fill("shaista.afreen@cmr.edu.in")
    page.get_by_role("button", name="Sign in").click()

    
    page.get_by_role("button", name="Dashboard Tools").click()
    page.get_by_role("button", name="Open Inventory Management").click()
    page.get_by_role("button", name="Inventory Management").click()
    page.get_by_role("button", name="View Product Inventory").click()


    while True:
        previous_count = page.locator("div:has-text('ID: ')").count()
        page.mouse.wheel(0, 5000)  
        page.wait_for_timeout(2000)  
        new_count = page.locator("div:has-text('ID: ')").count()

        if new_count == previous_count:  
            break

   
    product_data = extract_product_data(page)

    
    save_to_json(product_data)

    print("✅ Product inventory saved to 'product_inventory.json'!")

    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
