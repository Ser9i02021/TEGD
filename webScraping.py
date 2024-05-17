import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from time import sleep

# Certifique-se de que o caminho do ChromeDriver está correto
chrome_driver_path = "/Users/ser910/Documents/TEGD/chromedriver"

# Configure o ChromeDriver
options = Options()
options.add_argument("--headless")  # Rodar em modo headless (sem interface gráfica)
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL da página
url = 'https://www.metoffice.gov.uk/weather/forecast/6gj7ng0qu#?date=2024-04-25'

# Função principal para coletar dados
def scrape_weather_data():
    driver.get(url)
    sleep(3)  # Esperar a página carregar
    content = driver.page_source

    # Criar um objeto BeautifulSoup e analisar o HTML
    soup = BeautifulSoup(content, 'html.parser')

    class WeatherConditions:

        def summary_weather_conditions(self, day: int):
            tab = soup.find('li', {'data-tab-index': str(day)})

            weather_summary_elem = tab.find('div', class_='summary-text hide-xs-only')
            ws = weather_summary_elem.text.strip() if weather_summary_elem else 'No summary of weather conditions found'

            sunrise_time_elem = tab.find('div', class_='weather-text sunrise-sunset')
            sunrise_time = sunrise_time_elem.text.strip() if sunrise_time_elem else 'No sunrise time found'

            sunset_time_elem = tab.find('div', class_='weather-text sunrise-sunset sunset')
            sunset_time = sunset_time_elem.text.strip() if sunset_time_elem else 'No sunset time found'

            return {
                "day": day,
                "sunrise_time": sunrise_time,
                "sunset_time": sunset_time,
                "weather_summary": ws
            }

        def min_max_temps(self, day: int):
            tab = soup.find('li', {'data-tab-index': str(day)})

            max_temp_element = tab.find('span', class_='tab-temp-high')
            max_temp = max_temp_element.text.strip() if max_temp_element else 'No max temp found'

            min_temp_element = tab.find('span', class_='tab-temp-low')
            min_temp = min_temp_element.text.strip() if min_temp_element else 'No min temp found'

            return {
                "day": day,
                "max_temp": max_temp,
                "min_temp": min_temp
            }

        def all_temps_for_day(self, day: int):
            day = str(day)
            temperature_cells = soup.find_all('td', headers=lambda value: value and value.startswith('d' + day + 'Temp'))

            temperature_data = {}
            for cell in temperature_cells:
                time = cell['data-test-label'].split('T')[1].split(':')[0]
                time = int(time)
                if time < 3:
                    time += 24
                time -= 3
                time = str(time) + 'h'
                temperature = cell.div.get_text(strip=True)
                temperature_data[time] = temperature

            return temperature_data

    weather_conditions = WeatherConditions()

    # Coletar dados para 7 dias
    data = []
    for day in range(7):
        summary = weather_conditions.summary_weather_conditions(day)
        min_max = weather_conditions.min_max_temps(day)
        all_temps = weather_conditions.all_temps_for_day(day)

        data.append({
            "summary": summary,
            "min_max": min_max,
            "all_temps": all_temps
        })

    # Salvar os dados coletados em um arquivo JSON
    with open("weather_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Dados meteorológicos coletados e salvos com sucesso!")

# Executar a função de coleta de dados
scrape_weather_data()

# Fechar o driver
driver.quit()
