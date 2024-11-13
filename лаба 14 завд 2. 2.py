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
while True:
    print("Select an option:\n 1 - Enter the country\n 2 - Exit") 
    x = input("Choose an option:\n")
    x = int(x)

    if x == 1:
        ask = input("Enter the country (Iceland/India)\n")

        if ask == "Iceland":
            plt.bar(years_iceland, values_iceland, label='Iceland', color="blue")
        elif ask == "India":
            plt.bar(years_india, values_india, label='India', color="orange")
        else:
            print("You entered uncorrect word")

        plt.title('Age Dependency Ratio (% of working-age population)', fontsize=15)
        plt.xlabel('Year', fontsize=12, color='red')
        plt.ylabel('Dependency Ratio', fontsize=12, color='red')
        plt.legend()
        plt.grid(True)
        plt.show()

    elif x == 2:
        quit(0)
