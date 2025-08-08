# #!/usr/bin/env python
import argparse
import os
import shutil
import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options


def login(driver, website, user, password):
    """ Login to the website with provided user credentials"""
    print("Starting the browser...")

    # Navigate to the specified URL using `driver.get()`.
    driver.get(website)

    # Log in to the website
    # Enter the username
    driver.find_element(By.ID, "user-name").send_keys(user)
    # Enter the password
    driver.find_element(By.ID, "password").send_keys(password)
    # Click the login button
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("Login successful!")


def add_items_to_cart(driver):
    """ Add all items to the cart and verify the cart count"""
    # Find all item containers
    item_containers = driver.find_elements(By.CLASS_NAME, "inventory_item")
    cart_count = 0
    for item in item_containers:
        # Click the "Add to Cart" button for each item
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item.find_element(By.CLASS_NAME, "btn_inventory").click()
        print(f"Added {item_name} to cart")
        cart_count += 1
        time.sleep(2)
    print(f"Total items added to cart: {cart_count}")

    time.sleep(2)

    # Verify the cart count
    cart_badge_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert (int(cart_badge_count) == cart_count), f"Expected {cart_count} items in cart, but found {cart_badge_count}"
    print("All items added to cart successfully")


def remove_items_from_cart(driver):
    """ Remove all items from the cart and verify the cart count"""
    print("Removing items from cart...")
    print("Navigating to the cart...")
    # Navigate to the cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )
    
    # Find all cart items in containers
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    remove_count = 0
    for item in cart_items:
        # Click the "Remove" button for each item
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item.find_element(By.CLASS_NAME, "btn_secondary").click()
        print(f"Removed {item_name} from cart")
        remove_count += 1
        time.sleep(2)

    print(f"Total items removed from cart: {remove_count}")
    
    time.sleep(4)

    # Verify the cart is empty
    assert (len(cart_items) == remove_count), "Cart is not empty after removing items"
    print("All items removed from cart successfully")


def main():
    parser = argparse.ArgumentParser(description="Run Selenium")
    parser.add_argument("--headless", action="store_true", help="Run Chrome in headless mode")
    args = parser.parse_args()

    profile_dir = args.profile_dir or tempfile.mkdtemp(prefix="selenium_profile_")
    runtime_dir = args.runtime_dir or tempfile.mkdtemp(prefix="selenium_runtime_")
    os.environ["XDG_RUNTIME_DIR"] = runtime_dir

    options = Options()
    if args.headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
    
    options.add_argument(f"--user-data-dir=/tmp/selenium_user_data_{os.getpid()}")

    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-features=TranslateUI")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=0")

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    })
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        login(driver,"https://www.saucedemo.com/", "standard_user", "secret_sauce")
        add_items_to_cart(driver)
        time.sleep(2)
        remove_items_from_cart(driver)

        print("Test completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

    finally:
        if driver:
            print("Closing browser...")
            driver.quit()
        if not args.profile_dir:
            shutil.rmtree(profile_dir, ignore_errors=True)
        if not args.runtime_dir:
            shutil.rmtree(runtime_dir, ignore_errors=True)


if __name__ == "__main__":
    main()