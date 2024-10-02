from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")  # Required for running as root in some systems
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_service = Service("/usr/local/bin/chromedriver")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

time.sleep(5) 

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
