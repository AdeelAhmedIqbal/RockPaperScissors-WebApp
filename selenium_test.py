from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open your web app (adjust the URL to the correct one if necessary)
print("Opening the web app...")
driver.get("http://localhost")

# Find the start button using By.ID and click it
start_button = driver.find_element(By.ID, "start")
print("Clicking the start button...")
start_button.click()

# Wait for the game to finish
print("Waiting for the game to finish...")
time.sleep(7)

# Find the left and right containers by their IDs
left_container = driver.find_element(By.ID, "left")
right_container = driver.find_element(By.ID, "right")

# Check if both containers are displayed (indicating the game result is shown)
assert left_container.is_displayed() or right_container.is_displayed(), "Game result did not appear!"

print("Test passed! Game result appeared!")

# Close the browser
driver.quit()
