import json
import pandas as pd
import matplotlib.pyplot as plt

# Concatenate the contents of all JSON files to collect weather data from all the days avalilable in the research

# Load the first JSON file
with open('w_data_2.json', 'r', encoding='utf-8') as file:
    data1 = json.load(file)

# Load the second JSON file
with open('w_data_3.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

# Load the third JSON file
with open('w_data_6.json', 'r', encoding='utf-8') as file:
    data3 = json.load(file)

# Combine the three lists
data = data1 + data2 + data3

# Convert the list to a pandas DataFrame
df = pd.json_normalize(data)

cities_by_country = {
    "United Kingdom": [
        'London', 'Bath', 'Bradford', 'Brighton and Hove', 'Birmingham', 'Bristol', 'Cambridge', 'Canterbury',
        'Carlisle', 'Chelmsford', 'Chester', 'Chichester', 'Coventry', 'Derby', 'Doncaster', 'Durham', 'Ely',
        'Exeter', 'Gloucester', 'Hereford', 'Kingston upon Hull', 'Lancaster', 'Leeds', 'Leicester', 'Lichfield',
        'Lincoln', 'Liverpool', 'Manchester', 'Milton Keynes', 'Newcastle upon Tyne', 'Norwich', 'Nottingham',
        'Oxford', 'Peterborough', 'Plymouth', 'Portsmouth', 'Preston', 'Ripon', 'Salford', 'Salisbury', 'Sheffield',
        'Southampton', 'Southend-on-Sea', 'St Albans', 'Stoke-on-Trent', 'Sunderland', 'Truro', 'Wakefield', 'Wells',
        'Westminster', 'Winchester', 'Wolverhampton', 'Worcester', 'York', 'Aberdeen', 'Dundee', 'Edinburgh', 'Glasgow',
        'Inverness', 'Perth', 'Stirling', 'Bangor', 'Cardiff', 'Newport', 'St Asaph', 'St Davids', 'Swansea', 'Wrexham',
        'Armagh', 'Belfast', 'Derry (Londonderry)', 'Lisburn', 'Newry'
    ],
    "Ireland": [
        'Cork', 'Dublin', 'Galway', 'Kilkenny', 'Limerick', 'Waterford'
    ],
    "Belgium": [
        'Antwerp', 'Bruges', 'Brussels', 'Ghent'
    ],
    "Netherlands": [
        'Amsterdam', 'Rotterdam', 'Utrecht', 'Eindhoven', 'Tilburg', 'Groningen', 'Breda', 'Arnhem', 'Maastricht',
        'Dordrecht'
    ],
    "Denmark": [
        'Copenhagen', 'Aarhus', 'Odense', 'Aalborg', 'Esbjerg', 'Kolding', 'Horsens', 'Vejle'
    ],
    "Germany": [
        'Berlin', 'Hamburg', 'Munich', 'Frankfurt', 'Stuttgart', 'Dortmund', 'Essen', 'Leipzig', 'Bremen', 'Dresden',
        'Hannover', 'Duisburg'
    ],
    "Poland": [
        'Warsaw'
    ],
    "France": [
        'Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille',
        'Rennes', 'Reims', 'Le Havre', 'Toulon', 'Angers', 'Grenoble', 'Dijon', 'Brest', 'Limoges', 'Tours', 'Perpignan'
    ],
    "Luxembourg": [
        'Luxembourg City (Luxembourg)', 'Ettelbruck'
    ],
    "Norway": [
        'Oslo', 'Bergen', 'Trondheim', 'Stavanger', 'Drammen', 'Kristiansand', 'Sandnes'
    ],
    "Switzerland": [
        'Zurich (Zürich)', 'Geneva (Genève)', 'Basel', 'Lausanne'
    ],
    "Italy": [
        'Rome (Roma)', 'Milan (Milano)', 'Naples (Napoli)', 'Turin (Torino)', 'Palermo', 'Genoa (Genova)', 'Bologna',
        'Florence (Firenze)', 'Bari', 'Catania', 'Venice (Venezia)', 'Verona', 'Messina', 'Trieste', 'Taranto', 'Brescia',
        'Parma', 'Reggio Calabria', 'Perugia', 'Ravenna'
    ]
}

# Function to calculate the mean temperature for each row
def calculate_mean_temp(row):
    max_temp = int(row['min_max.max_temp'].replace('°', ''))
    min_temp = int(row['min_max.min_temp'].replace('°', ''))
    return (max_temp + min_temp) / 2

def mean_temp_for_all_regions():
    for region, cities in cities_by_country.items(): 
        # Filter the DataFrame to include only rows for the region's cities
        df_region = df[df['city'].isin(cities_by_country[region])].copy()

        # Apply the function to calculate the UV level for each row
        df_region['mean_temp'] = df_region.apply(calculate_mean_temp, axis=1)

        # Group by city and day to get the mean temperature for each city each day
        df_mean_temps = df_region.groupby(['city', 'day'])['mean_temp'].mean().reset_index()

        # Group by day to get the overall mean temperature across all cities for each day
        df_overall_mean_temps = df_mean_temps.groupby('day')['mean_temp'].mean().reset_index()

        # Calculate the mean temperature for the given period
        mean_temp = df_overall_mean_temps['mean_temp'].mean()

        print("Mean temperature for %s from 2024/05/31 to 2024/06/18: %f" % (region, mean_temp))



def mean_UV_level_for_all_regions():
    # Create an empty list to store UV values
    all_uv_values = []

    for region, cities in cities_by_country.items(): 
        # Filter the DataFrame to include only rows for the region's cities
        df_region = df[df['city'].isin(cities_by_country[region])].copy()

        # Extract the UV values for the region
        uv_values = df_region['summary.UV_value'].astype(float)

        # Calculate the mean UV value for the region
        mean_uv = uv_values.mean()

        print("Mean UV value for %s from 2024/05/31 to 2024/06/05: %f" % (region, mean_uv))



mean_temp_for_all_regions()
mean_UV_level_for_all_regions() 
