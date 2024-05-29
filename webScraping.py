import requests
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
new_cities = {
    'London': 'https://www.metoffice.gov.uk/weather/forecast/gcpvj0v07#?date=2024-05-29',
    'Bath': 'https://www.metoffice.gov.uk/weather/forecast/gcnk62de6#?date=2024-05-29',
    'Bradford': 'https://www.metoffice.gov.uk/weather/forecast/gcwdpcpzj',
    'Brighton and Hove': 'https://www.metoffice.gov.uk/weather/forecast/gcpcq5541',
    'Birmingham': 'https://www.metoffice.gov.uk/weather/forecast/gcqdt4b2x',
    'Bristol': 'https://www.metoffice.gov.uk/weather/forecast/gcnhtnumz',
    'Cambridge': 'https://www.metoffice.gov.uk/weather/forecast/u1214b469',
    'Canterbury': 'https://www.metoffice.gov.uk/weather/forecast/u10g8x4vg',
    'Carlisle': 'https://www.metoffice.gov.uk/weather/forecast/gcvbs84rv#?date=2024-05-29',
    'Chelmsford': 'https://www.metoffice.gov.uk/weather/forecast/u10q6cgzm#?date=2024-05-29',
    'Chester': 'https://www.metoffice.gov.uk/weather/forecast/gcmyw5w26#?date=2024-05-29',
    'Chichester': 'https://www.metoffice.gov.uk/weather/forecast/gcp3nqsgd#?date=2024-05-29',
    'Coventry': 'https://www.metoffice.gov.uk/weather/forecast/gcqfjkq3z#?date=2024-05-29',
    'Derby': 'https://www.metoffice.gov.uk/weather/forecast/gcqvn6pq4#?date=2024-05-29',
    'Doncaster': 'https://www.metoffice.gov.uk/weather/forecast/gcx0qr7rt#?date=2024-05-29',
    'Durham': 'https://www.metoffice.gov.uk/weather/forecast/gcwzefp2c#?date=2024-05-29',
    'Ely': 'https://www.metoffice.gov.uk/weather/forecast/gcjsyk4mw#?nearestTo=Ely%20(Cardiff)&date=2024-05-29',
    'Exeter': 'https://www.metoffice.gov.uk/weather/forecast/gcj2x8gt4#?date=2024-05-29',
    'Gloucester': 'https://www.metoffice.gov.uk/weather/forecast/gcnrj1e0w#?date=2024-05-29',
    'Hereford': 'https://www.metoffice.gov.uk/weather/forecast/gcq04hx21#?date=2024-05-29',
    'Kingston upon Hull': 'https://www.metoffice.gov.uk/weather/forecast/gcxcb25c4#?date=2024-05-29',
    'Lancaster': 'https://www.metoffice.gov.uk/weather/forecast/gcw52qce5#?date=2024-05-29',
    'Leeds': 'https://www.metoffice.gov.uk/weather/forecast/gcwfhf1w0#?date=2024-05-29',
    'Leicester': 'https://www.metoffice.gov.uk/weather/forecast/gcr5qn5jy#?date=2024-05-29',
    'Lichfield': 'https://www.metoffice.gov.uk/weather/forecast/gcqewq76c#?date=2024-05-29',
    'Lincoln': 'https://www.metoffice.gov.uk/weather/forecast/gcrwgdr98#?date=2024-05-29',
    'Liverpool': 'https://www.metoffice.gov.uk/weather/forecast/gcmzggpxq#?date=2024-05-29',
    'Manchester': 'https://www.metoffice.gov.uk/weather/forecast/gcw2hzs1u#?date=2024-05-29',
    'Milton Keynes': 'https://www.metoffice.gov.uk/weather/forecast/gcr2nc3b7#?date=2024-05-29',
    'Newcastle upon Tyne': 'https://www.metoffice.gov.uk/weather/forecast/gcybg0rne#?date=2024-05-29',
    'Norwich': 'https://www.metoffice.gov.uk/weather/forecast/u12gmt1fz#?date=2024-05-29',
    'Nottingham': 'https://www.metoffice.gov.uk/weather/forecast/gcrjp3v96#?date=2024-05-29',
    'Oxford': 'https://www.metoffice.gov.uk/weather/forecast/gcpn7mp10#?date=2024-05-29',
    'Peterborough': 'https://www.metoffice.gov.uk/weather/forecast/gcrg49fhe#?date=2024-05-29',
    'Plymouth': 'https://www.metoffice.gov.uk/weather/forecast/gbvn9cv4h#?date=2024-05-29',
    'Portsmouth': 'https://www.metoffice.gov.uk/weather/forecast/gcp0zn6wn#?date=2024-05-29',
    'Preston': 'https://www.metoffice.gov.uk/weather/forecast/gcw1fe28j#?date=2024-05-29',
    'Ripon': 'https://www.metoffice.gov.uk/weather/forecast/gcwgvr0fn#?date=2024-05-29',
    'Salford': 'https://www.metoffice.gov.uk/weather/forecast/gcw279prq#?date=2024-05-29',
    'Salisbury': 'https://www.metoffice.gov.uk/weather/forecast/gcndx0wq3#?date=2024-05-29',
    'Sheffield': 'https://www.metoffice.gov.uk/weather/forecast/gcqzwtdw7#?date=2024-05-29',
    'Southampton': 'https://www.metoffice.gov.uk/weather/forecast/gcp185f25#?date=2024-05-29',
    'Southend-on-Sea': 'https://www.metoffice.gov.uk/weather/forecast/u10t0nxqf#?date=2024-05-29',
    'St Albans': 'https://www.metoffice.gov.uk/weather/forecast/gcpy2m1yy#?date=2024-05-29',
    'Stoke-on-Trent': 'https://www.metoffice.gov.uk/weather/forecast/gcqmw2y12#?date=2024-05-29',
    'Sunderland': 'https://www.metoffice.gov.uk/weather/forecast/gcz02e3x2#?date=2024-05-29',
    'Truro': 'https://www.metoffice.gov.uk/weather/forecast/gbumvn49q#?date=2024-05-29',
    'Wakefield': 'https://www.metoffice.gov.uk/weather/forecast/gcwcmu8w8#?date=2024-05-29',
    'Wells': 'https://www.metoffice.gov.uk/weather/forecast/gcn57f71q#?date=2024-05-29',
    'Westminster': 'https://www.metoffice.gov.uk/weather/forecast/gcpuuyzwv#?date=2024-05-29',
    'Winchester': 'https://www.metoffice.gov.uk/weather/forecast/gcp46pp1c#?date=2024-05-29',
    'Wolverhampton': 'https://www.metoffice.gov.uk/weather/forecast/gcq7pt4g5#?date=2024-05-29',
    'Worcester': 'https://www.metoffice.gov.uk/weather/forecast/gcq2vmx21#?date=2024-05-29',
    'York': 'https://www.metoffice.gov.uk/weather/forecast/gcx4zrw25#?date=2024-05-29'
}

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

        uv_elem = tab.find('span', {'data-type': 'uv'})
        if uv_elem:
            uv_label = uv_elem['data-category']
            uv_value = uv_elem['data-value']
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

def get_data_and_wrap_it_to_JSON(from_item: int, to_item: int):
    data = []

    # Load existing data if the JSON file exists
    if os.path.exists("w_data.json"):
        with open("w_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    for city, url in dict(list(new_cities.items())[from_item:to_item]).items():
        weather_conditions = WeatherConditions(url)
        # Collect data for 7 days
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
                "city": city,
                "day": date,
                "summary": summary,
                "min_max": min_max,
                "all_temps_and_chances_of_rain": all_temps_and_chances_of_rain
            })

    # Save the collected data to a JSON file
    with open("w_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Weather data collected and saved successfully!")

# Collect and save weather data to JSON
for i in range(10, 53, 2):
    get_data_and_wrap_it_to_JSON(i, i + 2)

# Close the driver
driver.quit()
