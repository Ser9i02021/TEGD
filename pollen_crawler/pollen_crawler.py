from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
from selenium.webdriver.chrome.options import Options


# Ensure the path to ChromeDriver is correct
chrome_driver_path = "/Users/pc/Downloads/TEGD-main/chromedriver.exe"

# Configure ChromeDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Hide WebDriver attribute in navigator object
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

driver.get('https://www.metoffice.gov.uk/weather/forecast/gcpvj0v07')

# Wait until the Pollen icon is visible and clickable
try:
    pollen_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Pollen forecast for today']"))
    )
    # Click the Pollen icon
    pollen_element.click()
    time.sleep(2)  # Wait for the new page to load

except Exception as e:
    print(f"Error finding or clicking the Pollen icon: {e}")
    driver.quit()

# Now that we are on the new page, let's parse it with BeautifulSoup
new_page_html = driver.page_source
soup = BeautifulSoup(new_page_html, 'html.parser')

# For example, let's extract the title of the new page
title = soup.find('title').text
print(f"Title of the new page: {title}")

# Let's extract the pollen levels for each UK region for the next 4 days, plus today
def extract_pollen_data():
    try:
        
        new_page_html = driver.page_source
        soup = BeautifulSoup(new_page_html, 'html.parser')

        # Dictionary to store the data
        pollen_data = {}

        # Locate all pollen forecast cards
        forecast_cards = soup.find_all('div', class_='pollen-forecast-card')
        
        for card in forecast_cards:
            region_name = card.find('h3', class_='region-heading').text
            date_heading = card.find('h3', class_='date-heading').text
            last_issued = card.find('p', class_='last-issued').text
            
            # Dictionary to store data for a specific region
            region_data = {
                "date": date_heading,
                "last_issued": last_issued,
                "pollen_levels": {}
            }
            
            # Extract pollen levels for each day
            days = card.select('table thead th')
            pollen_levels = card.select('table tbody td .icon')

            for day, level in zip(days, pollen_levels):
                day_name = day.text.strip()
                pollen_level = level['title']
                region_data["pollen_levels"][day_name] = pollen_level
            
            # Add region data to the main dictionary
            pollen_data[region_name] = region_data

        # Write the data to a JSON file
        with open('w_data_pollen_5.json', 'w') as json_file:
            json.dump(pollen_data, json_file, indent=4)

        print("Data has been successfully saved to w_data_pollen.json")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    extract_pollen_data()
