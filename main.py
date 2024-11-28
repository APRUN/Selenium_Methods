from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Setup WebDriver
driver = webdriver.Chrome()

# Load page
try:
    driver.get("https://www.saucedemo.com/")
    print("Implemented .get(url) successfully!")
except:
    print("Error: Unable to load page.")
    driver.quit()
    exit()

# Minimize Window
driver.minimize_window()()
print("implemented minimize_window() Window successfully!")
time.sleep(2)

# Maximize Window
driver.maximize_window()
print("implemented maximize_window() Window successfully!")
time.sleep(2)

# Print Current URL
print("Current URL: ", driver.current_url)
time.sleep(2)

# Refresh Page
driver.refresh()
print("implemented refresh() Page successfully!")


assert "Dashboard" in driver.title, "Login failed!"
print("Login test executed successfully!")


driver.quit()