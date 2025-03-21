from playwright.sync_api import sync_playwright
import json
import os
from typing import Dict, List
import time

class ProductScraper:
    def __init__(self, login_url: str, challenge_url: str, username: str, password: str):
        self.login_url = login_url
        self.challenge_url = challenge_url
        self.username = username
        self.password = password
        self.session_file = "session.json"

    def authenticate(self, page) -> None:
        """Handle login process."""
        try:
            print("Starting authentication process...")
            
            # Navigate to login page
            print(f"Navigating to {self.login_url}")
            page.goto(self.login_url)
            page.wait_for_load_state("networkidle")
            
            # Wait for the login form elements
            print("Waiting for login form...")
            email_input = page.wait_for_selector("input[type='email']", 
                                               state="visible", 
                                               timeout=10000)
            password_input = page.wait_for_selector("input[type='password']", 
                                                  state="visible", 
                                                  timeout=10000)
            
            # Fill in credentials
            print("Filling credentials...")
            email_input.fill(self.username)
            password_input.fill(self.password)
            
            # Click the "Sign in" button
            print("Clicking Sign in button...")
            sign_in_button = page.get_by_text("Sign in", exact=True)
            sign_in_button.click()
            
            # Wait for navigation after login
            print("Waiting for navigation after login...")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(5000)  # Wait 5 seconds after login
            
            # Navigate directly to challenge URL after login
            print("Navigating to challenge page...")
            page.goto(self.challenge_url)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(3000)
            
        except Exception as e:
            print(f"Login failed with error: {str(e)}")
            page.screenshot(path="login_error.png")
            raise

    def navigate_to_products(self, page) -> None:
        """Navigate to the products page."""
        try:
            print("Waiting for Start Journey button...")
            
            # Wait for the button to be visible and clickable
            start_button = page.wait_for_selector("text=Start Journey", 
                                                state="visible",
                                                timeout=10000)
            if start_button:
                print("Found Start Journey button, clicking...")
                start_button.click()
                print("Clicked Start Journey button")
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(3000)
            else:
                raise Exception("Start Journey button not found")
            
            # Take screenshot for verification
            page.screenshot(path="after_start_journey.png")
            
        except Exception as e:
            print(f"Navigation failed with error: {str(e)}")
            page.screenshot(path="navigation_error.png")
            raise

    def run(self) -> None:
        """Main execution method."""
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=False,
                slow_mo=1000  # Slow down operations for debugging
            )
            
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080}
            )
            
            page = context.new_page()
            
            try:
                # Perform login
                self.authenticate(page)
                
                # Navigate to products
                self.navigate_to_products(page)
                
                # Keep browser open for debugging
                print("Navigation completed. Keeping browser open for 30 seconds...")
                page.wait_for_timeout(30000)  # Keep open for 30 seconds
                
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                page.screenshot(path="error.png")
            finally:
                # Add a delay before closing
                time.sleep(5)
                context.close()
                browser.close()

    def save_session(self, session_data: Dict) -> None:
        """Save session data to file."""
        try:
            with open(self.session_file, "w") as f:
                json.dump(session_data, f, indent=2)
        except Exception as e:
            print(f"Error saving session: {str(e)}")

    def load_session(self) -> Dict:
        """Load session data from file."""
        try:
            if os.path.exists(self.session_file):
                with open(self.session_file, "r") as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading session: {str(e)}")
        return None

    def save_products_to_json(self, products: List[Dict]) -> None:
        """Save extracted products to JSON file."""
        try:
            data = {
                "total_products": len(products),
                "extraction_date": time.strftime("%Y-%m-%d"),
                "products": products
            }
            
            with open("product_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            print(f"Successfully saved {len(products)} products to product_data.json")
        except Exception as e:
            print(f"Error saving to JSON: {str(e)}")

if __name__ == "__main__":
    # Configuration
    LOGIN_URL = "https://hiring.idenhq.com/"
    CHALLENGE_URL = "https://hiring.idenhq.com/challenge"
    USERNAME = "shaista.afreen@cmr.edu.in"   # Replace with actual username
    PASSWORD = "wbrdx6n0"    # Replace with actual password
    
    # Create and run scraper
    scraper = ProductScraper(LOGIN_URL, CHALLENGE_URL, USERNAME, PASSWORD)
    scraper.run()