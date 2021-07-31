foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

#1print(foods[0])
#2print(foods[4])
#3print(foods[-1])
#4print(foods[0:4])
#5print(foods[-3:12])
#6 confused

def Extract(rock):
    #return [foods[-1] for item in rock] #
    for item in rock:
       # print(item)
        #print (type(item))
        if type (item) == list: #== way of saying = , because = is assigning values
            x = item[-1]
    return x
print(Extract(foods))
