
import csv
from collections import defaultdict
import matplotlib.pyplot as plt


with open('population-estimates_csv.csv',newline='',encoding='ISO-8859-1') as csvfile:
    data= csv.DictReader(csvfile)
    saarc_population = {}
    countries = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]
    for row in data:
        if row["Region"] in countries:
            saarc_population[row["Year"]] = saarc_population.get(row["Year"],0) + int(float(row["Population"]))

    for i in saarc_population:
        print(i," : ",saarc_population[i])


    countries = list(saarc_population.keys())
    population = list(saarc_population.values())

    plt.bar(countries, population)
    plt.xlabel('Years')
    plt.ylabel('Population of the Country')
    plt.title('Population of SAARC Countries over years')
    plt.xticks(rotation = 45)
    plt.show()
