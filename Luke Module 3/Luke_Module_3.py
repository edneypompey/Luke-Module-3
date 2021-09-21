###### Luke Edney Tues 21 Sep 

###### 3.1.1.4
#write a simple two-line program that takes the parameter n as input, which is an integer, 
#and prints False if n is less than 100, and True if n is greater than or equal to 100

n = int(input("Type a number: ")) # allows the input after the string
print(n >= 100) #true/false reply if n greater or equal to 100

#####3.1.1.10

#Write a program that utilizes the concept of conditional execution, takes a string as input, and
#prints "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

flower = (input("What is your favourite plant? ")) #asks for user input
if flower == "Spathiphyllum": #if desired outcome then print as below
    print("Yes - Spathiphyllum is the best plant ever!")
elif flower == "spathiphyllum": #if its does not use the correct case the print below
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ", flower, "!", sep="") # otherwise print this

####3.1.1.11

#Your task is to write a tax calculator
#It should accept one floating-point value: the income
#Next it should print the calculated tax, rounded to full thalers. 
#There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
#If the calculated tax is less than zero, it only means no tax at all 
#(the tax is equal to zero). Take this into consideration during your calculations.

income = float(input("Enter the annual income: "))

if income <= 85528: #lower value of tax
    tax = income * .18 #finds 18 percent of the income (tax)
    tax = tax - 556.02 #minus the tax relief value of 556.02
else: 
    tax = 14839.02 #higher value of tax
    extra = income - 85528
    extra_tax = extra * .32 #finds 32 percent of the income (tax)
    tax = tax + extra_tax # add extra tex to tax
if tax < 0: # if tax is less than 0 not tax to be paid.
    tax =0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")