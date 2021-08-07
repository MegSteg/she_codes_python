groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon":9.00,
    "Carrots":0.56,
    "Oranges": 3.08
}
#add item
#groceries["avocados"] = 1.00
#print(groceries)

#remove an item
#del groceries["Bacon"]
#print(groceries)

#itering over the dictionary
#for item, price in groceries.items():
    #print(f'{item}: ${groceries[item]}')

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2 
    }

#for item in groceries:
   # calculation = round (groceries[item] * quantity[item], 2)
    #print(f"{quantity[item]} {item} @ $ {groceries[item]} = ${calculation}")


colour_counts = {
"blue": 0,
"green": 0,
"yellow": 0,
"red": 0,
"purple": 0,
"orange": 0,
}

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

#for item in colours: #iterating over a list
    #colour_counts[item]+=1
#for key, value in colour_counts.items(): #accessing the dict of colour counts using the name of the colour. Changing the value of that partic colour
    #print(f"{key}: {value}")

names = [
    "Maddy", 
    "Bel", 
    "Elnaz", 
    "Gia", 
    "Izzy",
    "Joy", 
    "Katie", 
    "Maddie", 
    "Tash", 
    "Nic",
    "Rachael", 
    "Bec", 
    "Bec", 
    "Tabitha", 
    "Teagen",
    "Viv", 
    "Anna", 
    "Catherine", 
    "Catherine", 
    "Debby",
    "Gab", 
    "Megan", 
    "Michelle", 
    "Nic", 
    "Roxy",
    "Samara", 
    "Sasha", 
    "Sophie", 
    "Teagen", 
    "Viv"
]

for item in names: #iterating over a list
    names[item]+=1
for key, value in names.items(): #accessing the dict of colour counts using the name of the colour. Changing the value of that partic colour
    print(f"{key}: {value}")



return (minimum, min_position)
    if len(weather_data) == 0:
        return()
    for i in range(0,len(weather_data)):
        max = round(float(max(weather_data)),1)
        max1 = weather_data.reverse()
        max1 = len(weather_data) - weather_data.index(max(weather_data)) -1
        return(max, max1)