from playwright_helper import PlaywrightHelper
import random
import string

def generate_unique_id():
    return ''.join(random.choices(string.digits, k=6))

def test_doctor_registration():
    # Initialize the browser with headless=False to see the automation
    browser = PlaywrightHelper(headless=False)
    
    # Generate unique identifier
    unique_id = generate_unique_id()
    
    try:
        url = "http://localhost:5001/doctor/register"
        # Navigate to the registration page (replace with actual URL)
        browser.navigate_to(url)
        
        # Fill in the registration form
        browser.type("input[name='first_name']", "Doctor")
        browser.type("input[name='last_name']", f"Test{unique_id}")
        browser.type("input[name='email']", f"doctor{unique_id}@example.com")
        browser.type("input[name='phone_number']", f"5555{unique_id}")
        browser.type("input[name='specialization']", "Cardiology")
        browser.type("input[name='password']", "SecurePass123!")
        
        # Select hospital from dropdown
        browser.select("select[name='hospital']", "1")  # Assuming "1" is a valid hospital ID
        
        # Click the register button
        browser.click("button[type='submit']")
        
        # Wait for success message or redirect
        # browser.wait_for(".success-message")  # Uncomment and adjust selector as needed
        
        # Take a screenshot
        browser.screenshot(f"doctor_registration_{unique_id}.png")
        
    finally:
        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_doctor_registration()
