import csv
from collections import defaultdict
import matplotlib.pyplot as plt


with open('population-estimates_csv.csv',newline='',encoding='ISO-8859-1') as csvfile:
    data= csv.DictReader(csvfile)
    india_population = {}
    for row in data:

        #Get the Region if it is India then get the population of that year.
        if(row["Region"] == "India"):
            india_population[row["Year"]] = int(float(row["Population"]))


    for i in india_population:
        print(i," : ",india_population[i]," ",type(india_population[i]))

    years = list(india_population.keys())
    registrations = list(india_population.values())

    plt.bar(years, registrations)
    plt.xlabel('Year')
    plt.ylabel('Population of the Year')
    plt.title('India Population')
    plt.xticks(rotation = 90)
    plt.show()