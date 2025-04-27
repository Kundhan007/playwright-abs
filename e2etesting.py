from playwright_helper import PlaywrightHelper
import random
import string
import pytest

@pytest.fixture(scope="module")
def browser_instance():
    browser = PlaywrightHelper(headless=False)
    yield browser
    browser.close()

def generate_unique_id():
    return ''.join(random.choices(string.digits, k=6))

def test_doctor_registration(browser_instance):
    browser = browser_instance
    unique_id = generate_unique_id()
    register_email = f"doctor{unique_id}@example.com"
    register_password = "SecurePass123!"

    try:
        url = "http://localhost:5001/doctor/register"
        browser.navigate_to(url)
        browser.type("input[name='first_name']", "Doctor")
        browser.type("input[name='last_name']", f"Test{unique_id}")
        browser.type("input[name='email']", register_email)
        browser.type("input[name='phone_number']", f"5555{unique_id}")
        browser.type("input[name='specialization']", "Cardiology")
        browser.type("input[name='password']", register_password)
        browser.select("select[name='hospital']", "1")
        browser.click("button[type='submit']")
        browser.page.wait_for_timeout(10000)
    except Exception as e:
        pytest.fail(f"Registration test failed: {e}")

def test_doctor_login_and_update(browser_instance):
    browser = browser_instance
    login_email = "doctor111181@example.com"
    login_password = "SecurePass123!"

    try:
        login_url = "http://localhost:5001/doctor/login"
        browser.navigate_to(login_url)
        browser.type("input[name='username_or_email']", login_email)
        browser.type("input[name='password']", login_password)
        browser.click("button[type='submit']")
        browser.page.wait_for_timeout(2000) # Wait for page/iframe to potentially load

        # --- Interact within the iframe --- 
        iframe_selector = 'iframe[name="content-frame-home"]'
        iframe = browser.page.frame_locator(iframe_selector)

        # Ensure the iframe is loaded/visible before interacting
        iframe.locator("form[action='/update_doctor']").wait_for(timeout=10000) # Wait for form inside frame
        
        update_form_selector = "form[action='/update_doctor']"
        email_input_selector = f"{update_form_selector} input[name='email']"
        save_button_selector = f"{update_form_selector} button[type='submit']"

        # Use iframe locator for elements inside the frame
        current_email = iframe.locator(email_input_selector).input_value()

        new_email = "doctor111181_new@example.com"
        iframe.locator(email_input_selector).fill("") # Clear field first
        iframe.locator(email_input_selector).type(new_email)

        iframe.locator(save_button_selector).click()

        # Wait for potential confirmation inside or outside the frame
        browser.page.wait_for_timeout(10000)

    except Exception as e:
        browser.screenshot(f"login_update_fail_{login_email}.png")
        pytest.fail(f"Login and update test failed (iframe interaction): {e}")

# ... (add the new login test below)

def test_doctor_registration_old_email(browser_instance):
    browser = browser_instance
    unique_id = generate_unique_id()
    register_email = 'doctor111181@example.com'
    register_password = "SecurePass123!"

    try:
        url = "http://localhost:5001/doctor/register"
        browser.navigate_to(url)
        browser.type("input[name='first_name']", "Doctor")
        browser.type("input[name='last_name']", f"Test{unique_id}")
        browser.type("input[name='email']", register_email)
        browser.type("input[name='phone_number']", f"5555{unique_id}")
        browser.type("input[name='specialization']", "Cardiology")
        browser.type("input[name='password']", register_password)
        browser.select("select[name='hospital']", "1")
        browser.click("button[type='submit']")
        browser.page.wait_for_timeout(10000)
    except Exception as e:
        pytest.fail(f"Registration test failed: {e}")
