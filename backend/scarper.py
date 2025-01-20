from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_crunchbase_data(driver_path):
    driver = webdriver.Chrome(driver_path)
    driver.get("https://www.crunchbase.com/")
    time.sleep(5)  # Wait for the page to load

    # Add login logic if required

    # Navigate to the organization page
    search_bar = driver.find_element(By.CLASS_NAME, "search-bar-class")  # Update selector
    search_bar.send_keys("Organizations")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)

    organizations = []
    org_elements = driver.find_elements(By.CLASS_NAME, "org-element-class")  # Update selector

    for org in org_elements:
        name = org.find_element(By.CLASS_NAME, "org-name-class").text  # Update selector
        location = org.find_element(By.CLASS_NAME, "org-location-class").text  # Update selector
        organizations.append({"name": name, "location": location})

    driver.quit()
    return organizations
