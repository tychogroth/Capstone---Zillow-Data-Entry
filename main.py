# Importing necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# URLs for Zillow and Google Sheets
ZILLOW_URL = "---"
GOOGLE_SHEETS = "---"

# Setting up Chrome options (headless mode, user-agent, and disabling certain features for bot detection avoidance)
options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Your User Agent String")
options.add_argument("--disable-blink-features=AutomationControlled")

# Initializing a Chrome driver with the specified options
driver = webdriver.Chrome(options=options)

# Navigating to the Zillow URL
driver.get(ZILLOW_URL)
# Pausing for 5 seconds to allow the page to fully load
time.sleep(5)

# Parsing the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Initializing an empty list to store listing details
listings = []

# Finding all property card elements on the page
article_tags = soup.find_all(attrs={"data-test": "property-card"})
# Looping through each property card, extracting details, and appending them to the listings list
for tag in article_tags:
    anchor_tag = tag.find("a")
    link = anchor_tag.get("href")
    price = str(tag.find(attrs={"data-test": "property-card-price"}).string)
    address = str(anchor_tag.string)
    house = {"link": link, "price": price, "address": address}
    listings.append(house)

# Looping through each listing to fill out and submit the Google Form
for house in listings:
    # Navigating to the Google Sheets URL
    driver.get(GOOGLE_SHEETS)
    # Pausing for 5 seconds to allow the page to fully load
    time.sleep(5)
    
    # Locating the input fields and submit button using XPATH
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # Filling out the form with the listing details
    address_input.send_keys(house["address"])
    price_input.send_keys(house["price"])
    link_input.send_keys(house["link"])
    # Clicking the submit button to submit the form
    submit_button.click()

    # Pausing for 5 seconds to allow the form submission to complete
    time.sleep(5)
