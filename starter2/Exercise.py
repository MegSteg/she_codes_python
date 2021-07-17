import csv

#Q1
with open("colours_20_simple.csv", mode = "r",) as csv_file:
    csv_reader= csv.reader(csv_file, 
    delimiter= ",")
    for donkey in csv_reader:
        print(f"{donkey[0]} {donkey[1]}{donkey[2]}")

#Q2
with open("colours_20_simple.csv", mode = "r",) as csv_file:
    csv_reader= csv.reader(csv_file, 
    delimiter= ",")
    for donkey in csv_reader:
        print(f"{donkey[2]} {donkey[1]}{donkey[0]}")

#Q3
parrots = []
with open("colours_20_simple.csv", mode = "r",) as csv_file:
    csv_reader= csv.reader(csv_file, 
    delimiter= ",")
    for donkey in csv_reader:
        #print(f"{donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")
parrots.append(donkey)
parrots.pop(0)

for donkey in parrots:
    print(f"{donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")
parrots.append(donkey)

#Q4 Opened file, assigned reader and now appending the data for line
data = []
with open("colours_20_simple.csv", mode = "r",) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter= ",")
    for line in csv_reader:
     data.append(line)

for colour in data:
     print(f"{colour[2]}")
     if "yellow" in colour[2]:
count= count+1
print(f"Red=0 Green: 0 Blue: 0 Yello:{count})
#repeat for all the colours 




