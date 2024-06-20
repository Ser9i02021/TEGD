import requests
from cities import City
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from time import sleep
import re
from datetime import datetime, timedelta
import os


# Ensure the path to ChromeDriver is correct
chrome_driver_path = "/Users/pc/Downloads/TEGD-main/chromedriver.exe"

# Configure ChromeDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Define the base URLs for the new cities
new_cities = City().cities

# Main class to collect data
class WeatherConditions:
    def __init__(self, url):
        driver.get(url)
        sleep(3)  # Wait for the page to load
        self.content = driver.page_source

        # Create a BeautifulSoup object and parse the HTML
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def get_forecast_date(self, day: int):
        tab = self.soup.find('li', {'data-tab-index': str(day)})
        if tab:
            return tab.get('data-tab-id', 'No date found')
        print(f"Error: No forecast tab found for day {day}")
        return None

    def summary_weather_conditions(self, day: int):
        tab = self.soup.find('li', {'data-tab-index': str(day)})
        if not tab:
            print(f"Error: Tab not found for day {day}")
            return {}

        weather_summary_elem = tab.find('div', class_='summary-text hide-xs-only')
        ws = weather_summary_elem.text.strip() if weather_summary_elem else 'No summary of weather conditions found'

        sunrise_time_elem = tab.find('div', class_='weather-text sunrise-sunset')
        sunrise_time = sunrise_time_elem.text.strip() if sunrise_time_elem else 'No sunrise time found'
        sunrise_time = re.search(r'\d{2}:\d{2}', sunrise_time).group(0) if re.search(r'\d{2}:\d{2}', sunrise_time) else 'No sunrise time found'

        sunset_time_elem = tab.find('div', class_='weather-text sunrise-sunset sunset')
        sunset_time = sunset_time_elem.text.strip() if sunset_time_elem else 'No sunset time found'
        sunset_time = re.search(r'\d{2}:\d{2}', sunset_time).group(0) if re.search(r'\d{2}:\d{2}', sunset_time) else 'No sunset time found'

        uv_elem = tab.find('span', {'data-type': 'uv'})
        if uv_elem:
            uv_label = uv_elem.get('data-category', 'No UV category')
            uv_value = uv_elem.get('data-value', 'No UV value')
        else:
            uv_label = 'No UV data found'
            uv_value = 'No UV data found'

        return {
            "weather_summary": ws,
            "sunrise_time": sunrise_time,
            "sunset_time": sunset_time,
            "UV_label": uv_label,
            "UV_value": uv_value
        }

    def min_max_temps(self, day: int):
        tab = self.soup.find('li', {'data-tab-index': str(day)})
        if not tab:
            print(f"Error: Tab not found for day {day}")
            return {}

        max_temp_element = tab.find('span', class_='tab-temp-high')
        max_temp = max_temp_element.text.strip() if max_temp_element else 'No max temp found'

        min_temp_element = tab.find('span', class_='tab-temp-low')
        min_temp = min_temp_element.text.strip() if min_temp_element else 'No min temp found'

        return {
            "max_temp": max_temp,
            "min_temp": min_temp
        }

    def all_temps_for_day(self, day: int):
        if self.soup is None:
            print("Soup object is not initialized properly.")
            return {}

        day_id = f"day{day}Header"
        day_header = self.soup.find('div', id=day_id)

        if not day_header:
            print(f"No header found for day {day}")
            return {}

        day_container = day_header.find_parent('div', class_='forecast-day')

        if not day_container:
            print(f"No forecast data found for day {day}")
            return {}

        temp_row = day_container.find('tr', class_='step-temp')

        if not temp_row:
            print(f"No temperature data found for day {day}")
            return {}

        time_row = day_container.find('tr', class_='step-time')

        if not time_row:
            print(f"No time data found for day {day}")
            return {}

        time_headers = time_row.find_all('th')
        times = [th.text.strip() for th in time_headers if 'data-time' in th.attrs]

        temp_cells = temp_row.find_all('td')
        temperatures = [cell.text.strip() for cell in temp_cells]

        temp_data = {}

        for time, temp in zip(times, temperatures):
            temp_data[time] = temp

        return temp_data

    def chance_of_precipitation(self, day: int):
        if self.soup is None:
            print("Soup object is not initialized properly.")
            return {}

        day_id = f"day{day}Header"
        day_header = self.soup.find('div', id=day_id)

        if not day_header:
            print(f"No header found for day {day}")
            return {}

        day_container = day_header.find_parent('div', class_='forecast-day')

        if not day_container:
            print(f"No forecast data found for day {day}")
            return {}

        precipitation_row = day_container.find('tr', class_='step-pop')

        if not precipitation_row:
            print(f"No precipitation data found for day {day}")
            return {}

        time_row = day_container.find('tr', class_='step-time')

        if not time_row:
            print(f"No time data found for day {day}")
            return {}

        time_headers = time_row.find_all('th')
        times = [th.text.strip() for th in time_headers if 'data-time' in th.attrs]

        precipitation_cells = precipitation_row.find_all('td')
        precipitation_chances = [cell.text.strip() for cell in precipitation_cells]

        chance_of_rain_data = {}

        for time, chance in zip(times, precipitation_chances):
            chance_of_rain_data[time] = chance

        return chance_of_rain_data

def get_data_and_wrap_it_to_JSON(from_item: int, to_item: int):
    data = []

    if os.path.exists("w_data_6.json"):
        with open("w_data_6.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    for city, url in dict(list(new_cities.items())[from_item:to_item]).items():
        print(f"Collecting data for {city} from {url}")
        weather_conditions = WeatherConditions(url)

        for day in range(6):
            date = weather_conditions.get_forecast_date(day)
            if not date:
                print(f"Error: No forecast date found for {city}, day {day}")
                continue

            summary = weather_conditions.summary_weather_conditions(day)
            min_max = weather_conditions.min_max_temps(day)
            all_temps = weather_conditions.all_temps_for_day(day)
            all_chances_of_rain = weather_conditions.chance_of_precipitation(day)

            all_temps_and_chances_of_rain = {}
            for time in all_temps.keys():
                all_temps_and_chances_of_rain[time] = {
                    "temperature": all_temps[time],
                    "chance_of_rain": all_chances_of_rain.get(time, "No data")
                }

            data.append({
                "city": city,
                "day": date,
                "summary": summary,
                "min_max": min_max,
                "all_temps_and_chances_of_rain": all_temps_and_chances_of_rain
            })

    with open("w_data_6.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Weather data collected and saved successfully! (%d - %d)" % (from_item, to_item))

for i in range(0, 167, 2):
    get_data_and_wrap_it_to_JSON(i, i + 2)

driver.quit() 
