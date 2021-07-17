import csv
from os import putenv

#population = []
#with open("2016_pilbara.csv") as csv_file:
    #csv_reader = csv.reader(csv_file) 
    #for line in csv_reader:
        population.append(line)

###print(population)

#for age_group in population:
    print(f"{age_group[0]}")

with open("population.csv", mode="w", newline="") as csv_file:
    csv_writer= csv.writer(csv_file)
    for age_group in population:
        csv_writer.writerow(["hi","hello"]) #ETRACTS FROM LIST AND WRITES THE SPECIFIED ELEMENTS