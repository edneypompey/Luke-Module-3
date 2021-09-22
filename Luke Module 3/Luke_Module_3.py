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

####3.1.1.12

#Since the introduction of the Gregorian calendar (in 1582), 
#the following rule is used to determine the kind of year:
#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.
#It would be good to verify if the entered year falls into the Gregorian era, 
#and output a warning otherwise: Not within the Gregorian calendar period.

year = int(input("Enter a year: "))

if year < 1582: #if less than 1582 then its is not within the Gregorian era and does not count
    print("Not within the Gregorian calendar period")
elif year % 4 != 0: #if the number cannot be divided by 4 then it will not be equal to 0. Its a common year.
      print("Common year")
elif year % 100 != 0: #if the number cannot be divided by 100 then it will not be equal to 0. Its a common year.
        print("Leap year")
elif year % 400 != 0: #if the number cannot be divided by 400 then it will not be equal to 0. Its a common year.
    print("Common year")
else:
    print("Leap year") #if it doesnt match the above then it must be a leap year.
  
#### Weds 22 Sep   

##### 3.2.1.3

#complete the code in the editor in such a way so that the code
#will ask the user to enter an integer number
#will use a while loop
#will check whether the number entered by the user is the same as the number picked by the magician
# if not prompt "Ha ha! You're stuck in my loop!"secret_number = 777
#if its correct prompt "Well done, muggle! You are free now."

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_guess =int(input("Enter a number: "))#create int variable from user input

while user_guess != secret_number: # while number is not the same as 777 print next line
    print("Ha ha! You're stuck in my loop!") # print this each time
    user_guess =int(input("Enter a diferent number: ")) # then prompt to ask a new number
    print("Well done, muggle! You are free now.") # when the while statement is false (eg = 777 print this)