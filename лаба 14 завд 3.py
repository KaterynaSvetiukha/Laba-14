import matplotlib.pyplot as plt
import csv

years_india = []
values_india = []

try:
    with open("work_age_population.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        
        for row in reader:
            if row['Time'] and row['Value']:
                year = int(row['Time'])
                value = float(row['Value'])

                if row['Country Name'] == 'India':
                    years_india.append(year)
                    values_india.append(value)
except FileNotFoundError:
    print("Файл work_age_population.csv не знайдено!")

# Побудова кругової діаграми
fig, ax = plt.subplots()
ax.pie(values_india, labels=years_india, autopct='%1.1f%%')
ax.axis("equal")
plt.legend(title="Роки", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()
