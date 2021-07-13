#Q1)
answer1 = input ("Enter a Number ")
answer2 = input ("Enter another number ")
calculation= int(answer1) + int(answer2)
print(str(calculation))

#Q1) COrrect because need .0 on numbers, so FLOAT
answer1 = input ("Enter a Number ")
answer2 = input ("Enter another number ")
calculation= float(answer1) + float(answer2)
print (calculation)

#Q2)Changed to float and correct print
answer1 = input ("Enter a Number ")
answer2 = input ("Enter another number ")
calculation= float(answer1) * float(answer2)
print('f*{answer1} * {answer2} = {calculation}')


#Q3) CHange to suit exactly the output, 24 and 25
answer1 = input ("How Many Kilometers? ")
calculation1= int(answer1) * 1000
calculation2= int(answer1) * 100000
message=(f"{answer1}km = {calculation1}m, {answer1}km ={calculation2}cm")
print(str(message))

#Q4)
name= input ("What is your name? ")
height= input ("How Tall are You (cms)? ")
message2= (f'{name} is {height}cms tall.')
print(message2)