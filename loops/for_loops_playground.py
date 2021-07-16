#a = [1,2,3,4]
#print (a[1:4])
# range is very similar

#for number in range (10): #iterate through sequence of numbers 0,2,3...9
    #print(number)

#for number in range (1,11): #now determining exact range
    #print(number)

#for number in range (1,11,2): #will now gor through each option by intervals of the third interger, in this case 2
    #print(number)

#for number in range(0,101):
    #print(number)

#for number in range(0,100,5):
    #print(number)

#letters = ["a","b","c","d"]

#result = ""

#for letter in letters:
    #result = result + letter
    #print(result)
#print(result)

#chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

#for item in range (len(chilli_wishlist)): 
    #print(chilli_wishlist[item])

##for item in chilli_wishlist:
    #print(item)

#Adapt tge for loop to print a message
#for each item in the list e.g. "Chilli wants: item"
#Use a for loop to print each item in a list
#from a previous exercise or example

#for item in chilli_wishlist:
    #print(f"Chilli wants:{item}") # variable name in curly brackets because in a formatted string

#names = ["Brooke", "Carlie", "Katie", "Stacey"]
#for name in names:
    #print(name)

#Nested Loops
numbers = [
    [1,2,3], #0 index
    [4], #1 index
    [5,6] #2 index
]

#print(numbers[2][-1]) #2 because 5,6 is the second index, -1 because it is the last element. MAKE SURE SEPERATE[]


chilli_wishlist = [
    ["igloo"], 
    ["chicken", "donut toy"],
    ["steak", "cardboard box"],
    ["kong"]
]

for category in chilli_wishlist:
    for item in category:
        print(item) #prints everything
