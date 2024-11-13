import numpy as np
import matplotlib.pyplot as plt
import csv

years_iceland = []
values_iceland = []
years_india = []
values_india = []

try:
    with open("work_age_population.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        
        for row in reader:
            if row['Time'] and row['Value']:
                year = int(row['Time'])
                value = float(row['Value'])
                
                if row['Country Name'] == 'Iceland':
                    years_iceland.append(year)
                    values_iceland.append(value)
                elif row['Country Name'] == 'India':
                    years_india.append(year)
                    values_india.append(value)
except FileNotFoundError:
    print("Файл work_age_population.csv не знайдено!")

# Побудова графіків для Ісландії та Індії
plt.plot(years_iceland, values_iceland, label='Iceland', color="blue")
plt.plot(years_india, values_india, label='India', color="orange")
plt.title('Age Dependency Ratio (% of working-age population)', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('Dependency Ratio (%)', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.show()
