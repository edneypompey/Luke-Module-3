###### Luke Edney Tues 21 Sep 

###### 3.1.1.4
# write a simple two-line program that takes the parameter n as input, which is an integer, 
# and prints False if n is less than 100, and True if n is greater than or equal to 100

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