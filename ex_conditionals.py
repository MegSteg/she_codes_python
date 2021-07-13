#Q1



moths_in_house = True
print(moths_in_house)
print(not moths_in_house)

if moths_in_house == True:
    print("Get the moths")
elif moths_in_house != True:
    print("No Threats Detected.")

#Q2
mitch_is_home = False
if (moths_in_house and mitch_is_home):
    print("Hoooman! Help me get the moths!")
elif (not moths_in_house and  not mitch_is_home):
    print("No Threats Detected.")
elif(moths_in_house and not mitch_is_home):
    print("Meooooooooooooow! Hissssss!")
elif(not moths_in_house and mitch_is_home ):
    print('Climb on Mitch.')

#Q3
light_colour = "Green"
car_detected = True

if light_colour == "Red" and car_detected == True:
    print("Flash!")
else:
    print("Do nothing")

#Q4
minheight= 120
answer= input("What is your height in cms? ")

if int(answer) > minheight:
    print("Hop on!")
elif int(answer) == minheight:
    print("Hope on!")
elif int(answer) < minheight:
    print("Sorry, not today :(")

#Q6
a = input("Please enter your email: ")

if "@" and "." in a:
    print("Valid email")
else:
    print("Invalid email")