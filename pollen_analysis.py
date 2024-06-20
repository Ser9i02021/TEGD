import json
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd

# Load the first JSON file
with open('w_data_pollen_2.json', 'r', encoding='utf-8') as file:
    data1 = json.load(file)

# Load the second JSON file
with open('w_data_pollen_5.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

# Extract pollen levels
pollen_levels1 = {region: details['pollen_levels'] for region, details in data1.items()}
pollen_levels2 = {region: details['pollen_levels'] for region, details in data2.items()}

combined_pollen_levels = {}

for region in pollen_levels1.keys():
    if region in pollen_levels2:

        pollen_levels_across_days = {}
        d = 13
        for day, level in pollen_levels1[region].items():
            pollen_levels_across_days[d] = level
            d += 1
        for day, level in pollen_levels2[region].items():
            pollen_levels_across_days[d] = level
            d += 1

        combined_pollen_levels[region] = pollen_levels_across_days

#print(combined_pollen_levels)

# Create a DataFrame from the dictionary
df = pd.DataFrame(combined_pollen_levels).T

# Convert pollen levels to numeric for plotting
level_map = {'Low pollen': 1, 'Moderate pollen': 2, 'High pollen': 3, 'Very high pollen': 4}
df = df.applymap(lambda x: level_map.get(x, 0))

# Plotting
plt.figure(figsize=(14, 10))

for region in df.index:
    plt.plot(df.columns, df.loc[region], marker='o', label=region)

    plt.xlabel('Day')
    plt.ylabel('Pollen Level')
    plt.title('Pollen Levels from Day 13 to Day 20')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Calculate the average pollen level for each region
average_pollen_levels = df.mean(axis=1)

# Plotting the average pollen levels
plt.figure(figsize=(14, 8))
average_pollen_levels.plot(kind='bar', color='skyblue')

plt.xlabel('Region')
plt.ylabel('Average Pollen Level')
plt.title('Average Pollen Level for Each Region from Day 13 to Day 20')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
