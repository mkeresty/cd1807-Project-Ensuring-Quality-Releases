# #!/usr/bin/env python
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

def reset_app_state(driver):
    """ Reset the application state by clearing cookies and local storage"""
    print("Resetting application state...")
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.refresh()



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
        time.sleep(1)
        cart_count += 1

    print(f"Total items added to cart: {cart_count}")
    time.sleep(1)
    return cart_count


def remove_items_from_cart(driver, cart_count):
    """ Remove all items from the cart and verify the cart count"""
    print("Removing items from cart...")
    print("Navigating to the cart...")
    # Navigate to the cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "[data-test^='cart-list']"))
    )

    
    # Find all cart items in containers
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert (cart_count == len(cart_items)), f"Expected {cart_count} items in cart, but found {len(cart_items)}"

    remove_count = 0
    for item in cart_items:
        # Click the "Remove" button for each item
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item.find_element(By.CLASS_NAME, "btn_secondary").click()
        print(f"Removed {item_name} from cart")
        time.sleep(1)
        remove_count += 1


    print(f"Total items removed from cart: {remove_count}")
    time.sleep(1)

    # Verify the cart is empty
    assert (len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0), "Cart is not empty after removing items"
    print("All items removed from cart successfully")


def make_driver():
    """Creates a Chrome driver with necessary options"""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
    })
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding")

    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-default-browser-check")


    return webdriver.Chrome(options=options)

def main():


    driver = None
    url = "https://www.saucedemo.com/"
    try:
        driver = make_driver()
        driver.get(url)
        reset_app_state(driver)
        login(driver, url, "standard_user", "secret_sauce")
        time.sleep(4)
        cart_count = add_items_to_cart(driver)
        time.sleep(1)
        remove_items_from_cart(driver, cart_count)

        print("Test completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

    finally:
        if driver:
            print("Closing browser...")
            driver.quit()


if __name__ == "__main__":
    main()