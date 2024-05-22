import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from time import sleep
import re

# Ensure the path to ChromeDriver is correct
chrome_driver_path = "/Users/pc/Downloads/TEGD-main/chromedriver.exe"

# Configure ChromeDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL of the page
url = 'https://www.metoffice.gov.uk/weather/forecast/6gj7ng0qu#?date=2024-04-25'

# Main class to collect data
class WeatherConditions():
    def __init__(self) -> None:
        driver.get(url)
        sleep(3)  # Wait for the page to load
        self.content = driver.page_source

        # Create a BeautifulSoup object and parse the HTML
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def get_forecast_date(self, day: int):
        tab = self.soup.find('li', {'data-tab-index': str(day)})
        if tab and 'data-tab-id' in tab.attrs:
            return tab['data-tab-id']
        return None

    def summary_weather_conditions(self, day: int):
        tab = self.soup.find('li', {'data-tab-index': str(day)})

        weather_summary_elem = tab.find('div', class_='summary-text hide-xs-only')
        ws = weather_summary_elem.text.strip() if weather_summary_elem else 'No summary of weather conditions found'

        sunrise_time_elem = tab.find('div', class_='weather-text sunrise-sunset')
        sunrise_time = sunrise_time_elem.text.strip() if sunrise_time_elem else 'No sunrise time found'

        # Use regular expression to extract time
        sunrise_time_match = re.search(r'\d{2}:\d{2}', sunrise_time)
        if sunrise_time_match:
            sunrise_time = sunrise_time_match.group(0)
        else:
            sunrise_time = 'No sunrise time found'

        sunset_time_elem = tab.find('div', class_='weather-text sunrise-sunset sunset')
        sunset_time = sunset_time_elem.text.strip() if sunset_time_elem else 'No sunset time found'

        # Use regular expression to extract time
        sunset_time_match = re.search(r'\d{2}:\d{2}', sunset_time)
        if sunset_time_match:
            sunset_time = sunset_time_match.group(0)
        else:
            sunset_time = 'No sunset time found'

        tab = self.soup.find('li', {'data-tab-index': str(day)})
        uv_elem = tab.find('span', {'data-type': 'uv'})
        if uv_elem:
            uv_label = uv_elem['data-category']
            uv_value = uv_elem['data-value']

        return {
            "weather_summary": ws,
            "sunrise_time": sunrise_time,
            "sunset_time": sunset_time,
            "UV_label": uv_label,
            "UV_value": uv_value
        }

    def min_max_temps(self, day: int):
        tab = self.soup.find('li', {'data-tab-index': str(day)})

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
            return

        # Locate the day-specific forecast element using id for header
        day_id = f"day{day}Header"
        day_header = self.soup.find('div', id=day_id)

        if not day_header:
            print(f"No header found for day {day}")
            return

        # Locate the parent container for the day's data
        day_container = day_header.find_parent('div', class_='forecast-day')

        if not day_container:
            print(f"No forecast data found for day {day}")
            return

        # Locate the row containing the temperatures within this day container
        temp_row = day_container.find('tr', class_='step-temp')

        if not temp_row:
            print(f"No temperature data found for day {day}")
            return

        # Locate the corresponding time row
        time_row = day_container.find('tr', class_='step-time')

        if not time_row:
            print(f"No time data found for day {day}")
            return

        # Extract the times from each <th> element within the time row
        time_headers = time_row.find_all('th')
        times = [th.text.strip() for th in time_headers if 'data-time' in th.attrs]

        # Extract the temperatures from each <td> element within the temperature row
        temp_cells = temp_row.find_all('td')
        temperatures = [cell.text.strip() for cell in temp_cells]

        temp_data = {}

        # Create a dictionary with time and temperature
        for time, temp in zip(times, temperatures):
            temp_data[time] = temp

        return temp_data

    def chance_of_precipitation(self, day: int):
        if self.soup is None:
            print("Soup object is not initialized properly.")
            return

        # Locate the day-specific forecast element using id for header
        day_id = f"day{day}Header"
        day_header = self.soup.find('div', id=day_id)

        if not day_header:
            print(f"No header found for day {day}")
            return

        # Locate the parent container for the day's data
        day_container = day_header.find_parent('div', class_='forecast-day')

        if not day_container:
            print(f"No forecast data found for day {day}")
            return

        # Locate the row containing the chance of precipitation within this day container
        precipitation_row = day_container.find('tr', class_='step-pop')

        if not precipitation_row:
            print(f"No precipitation data found for day {day}")
            return

        # Locate the corresponding time row
        time_row = day_container.find('tr', class_='step-time')

        if not time_row:
            print(f"No time data found for day {day}")
            return

        # Extract the times from each <th> element within the time row
        time_headers = time_row.find_all('th')
        times = [th.text.strip() for th in time_headers if 'data-time' in th.attrs]

        # Extract the chance of precipitation from each <td> element within the precipitation row
        precipitation_cells = precipitation_row.find_all('td')
        precipitation_chances = [cell.text.strip() for cell in precipitation_cells]

        chance_of_rain_data = {}

        # Print the extracted times and precipitation chances
        for time, chance in zip(times, precipitation_chances):
            chance_of_rain_data[time] = chance

        return chance_of_rain_data

def get_data_and_wrap_it_to_JSON():
    weather_conditions = WeatherConditions()
    # Collect data for 7 days
    data = []
    for day in range(7):
        # Get the forecast date from the source code
        date = weather_conditions.get_forecast_date(day)

        summary = weather_conditions.summary_weather_conditions(day)  # Sunrise and sunset times + overall weather condition for a given day
        min_max = weather_conditions.min_max_temps(day)  # Min and max temps for a given day
        all_temps = weather_conditions.all_temps_for_day(day)  # All temps for a given day
        all_chances_of_rain = weather_conditions.chance_of_precipitation(day)  # Chances of rain for a given day

        # Combine temperatures and chances of rain
        all_temps_and_chances_of_rain = {}
        for time in all_temps.keys():
            all_temps_and_chances_of_rain[time] = {
                "temperature": all_temps[time],
                "chance_of_rain": all_chances_of_rain.get(time, "No data")
            }

        # Append the data for each day as a separate entry in the JSON list
        data.append({
            "day": date,
            "summary": summary,
            "min_max": min_max,
            "all_temps_and_chances_of_rain": all_temps_and_chances_of_rain
        })

    # Save the collected data to a JSON file
    with open("weather_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Weather data collected and saved successfully!")

# Collect and save weather data to JSON
get_data_and_wrap_it_to_JSON()

# Close the driver
driver.quit()
