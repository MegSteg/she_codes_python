import csv

population = []
#with open("2016_pilbara.csv") as csv_file:
   # reader = csv.reader (csv_file)
   # for line in reader:
   #     population.append(line)
  #  print(population)

for age_group in population:
    print(f"{age_group[0]} {age_group[1]}")
with open ("population.csv", mode = "w", encoding = "utf-8") as csv_file:
    csv_writer=csv.writer(csv_file,delimiter=",")
print(population)