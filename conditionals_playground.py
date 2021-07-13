is_raining = False
is_cold = True

#print (is_raining)
#print(type(is_raining))
#print(is_cold)
#print(type(is_cold))

is_gym_open = True
is_sunny = False
#print(is_raining and is_cold)
#print(is_raining or is_cold)
#print (not is_raining)
#print(is_raining and not is_cold)

print(is_raining) #F
print(not is_raining) #T
print (is_raining or is_cold) #T
print (is_raining and not is_cold) #F
print(is_raining or not is_cold) #F
print(not is_raining and not is_cold) #F

print (5<3)
print (5>3)
print (10>=10)
print(4<=10)
print(5 == 5) 
print(5 != 4) #checks if not equal

print(5.1 > 2.4)

temperature= 16
print(temperature < 18)
wind_chill = 3
print(wind_chill > 4)
print (temperature - wind_chill < 16)

name = "Hayley"
print(name == "Hayley") 
print(name != "Hayley")

print ("A" > "a") #characters are stored in your computer as Aski characters and has a numerical value. Capitals have lower numerical value
print(ord("A"))
print("A" == 65)

#syntax/ semantics
#
name = "Asli"
if name == "Asli": #syntax if followed by a statement. : opens up the body for the 'if'
    print ("Hello Asli") #if says error, it need a tab following the :
    #so in above example, if 49 is true, than print 50.
elif name == "Randall": #elif comes after if, and is being check if the if statement before it is false
    print("Hi Randall")
else:  #will take care of all other conditions if not met here
    print("Hello")

if is_raining:
    print("Take an umbrella")
else:
    print("Do not take an umbrella")

temperature = 16
d_chill = 3
if temperature -wind_chill < 16:
    print("Take a jumper")
elif temperature - wind_chill > 30:
    print ("Fuck, it's hot today")
else:
    if is_raining:
        print("Wow, what a lovely day")
    if temperature- wind_chill < 16:
        print ("you'll need a jumper today.")

#nested statements

letters = ["a","b","c","d"] #they index list items in order, so a=0, b=1 etc.
letters[1]

letters = ["a","b","c","d"] #they index list items in order, so a=0, b=1 etc.
print(letters[3])
print(letters[-1]) #will always give us the very last value no matter how many
print(letters[-2]) #will give us second last letter
print(letters[0:3]) #tells computer where to start 
print(letters[0:3:1]) #shows starting index: when stopping( not inclusive of number stopping at): and increments of increase



chilli_wishlist = ["igloo", "chicken", "donut toy","cardboard box"]
# indexing
print(len(chilli_wishlist))
print(chilli_wishlist)
print(type(chilli_wishlist))

print(chilli_wishlist[3])
print(chilli_wishlist[0])
print(chilli_wishlist[1])
print(chilli_wishlist[-1])
print(chilli_wishlist[0:2])
print(chilli_wishlist[1:3])
chilli_wishlist[1] = 'carrot'