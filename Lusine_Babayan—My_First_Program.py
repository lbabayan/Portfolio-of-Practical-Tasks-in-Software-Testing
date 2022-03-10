from tkinter import N


print ("This is my first program!")
print("Lusine Babayan")

#About My Background in Short
#I have background in linguistics, which I love a lot.
#I have an MA degree in the field and a certificate in translation.

x=8
y=-5
z=x+y
print(z)
print(8+(-5))

#Variables (things to store and reuse later, like the token in Postman)
name = "Lusine"
age = 39
actual_age = 39.7
print(name)
print(age)
print("Hi, " + name + ".\n")

quantity = 15
price = 30
total = quantity * price
print(total)

#Function "type", data types
print(type(name))
print(type(age))
print(type(actual_age))
print("\n")

#Triple-quoated strings 
print ("""I would like to learn about your future plans.
I would like you tell me about your background.
Let's discuss some performance bottlnecks\n""")

#Concatenating
print("Hello, I am Lusine. " + "I am 39 years old. " + "I love learning new things.\n\n")

#Introducing a new line
print("There is a lot of technical stuff to learn.\n" "It is not always very easy to digest it.\n")

#Code multiplication
print("I am really serious to learn how to code." * 10 + "\n")

#Multiplication with backslash
print("I am really serious to learn how to code.\n" * 10)
print("")
 
# if-else statements
surname = "Benson"
if surname == "Benson":
    print("Hi, Mr Benson.\n")
else:
    print("Where is Mr Benson?\n")

surname = "Buckovsky"
if surname == "Dickens":
    print("Hi, Mr Dickens.\n")
else:
    print("Where is Mr Buckovsky?\n")

#input function (For user input I activated
#Integrated Terminal from Settings to be able to input data as user.)
number = input("Enter a number. ")
print(number)
(exit)

print("\n")
name_1 = input("What is your name?\n")
print(name_1)

print("\n")
#Small project "At the Robo_Bar" to combine all the above
#mentioned features and functions. The Robo barman asks questions
#and gives predefined answers.
cocktails = "Old Fashioned, Negroni, Whisky Highball"
plain_drinks = "Gin, Whisky, Vermouth "
print("Hello and welcome to my bar!")
order_0 = input("Would you like to drink cocktails or plain drinks? ")
if order_0 == "cocktails":
    print("Here is our cocktail menu! " + cocktails + "What would you like to drink?")
    order = input()
    print("Nice, choice, your "  + order + " would be ready in a moment.")
else:
    print("Here is the menu for our plain drinks: "  + plain_drinks +
    "Which do you prefer?")
    order_1 = input()
    print("Oh, " + order_1 + "!" + "That is my favorite! It will be ready in a moment!!!")

print("Have a nice day.\n")

#practicing
x = [-2, -9, -7, -1]
min = 3
if min > x[2]:
    print("Hello, world!")
else: 
    print("Go on.")