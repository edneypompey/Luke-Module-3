##### Luke Edney Tue 22 Sep ##### 

########2.1

##Original code
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    *\n", "  * *\n", " *   *\n","*     *","\n***   ***", "\n  *   *", "\n  *   *", "\n  *****")

#make the arrow twice as large (but keep the proportions)
print("         *")
print("        * *")
print("       *   *")
print("      *     *")
print("     *       *")
print("    *         *")
print("   *           *")
print("  *             *")
print(" *               *")
print("******       ******")
print("     *       *")
print("     *       *")
print("     *       *")
print("     *       *")
print("     *********")

#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2
print("    *     " *2)
print("   * *    " *2)
print("  *   *   " *2)
print(" *     *  " *2)
print("***   *** " *2)
print("  *   *   " *2)
print("  *   *   " *2)
print("  *****   " *2)

########2.2 literals

#Write a one-line piece of code, using the print() function, as well as the newline and escape characters:
print("\"I'm\"", "\n\"\"learning\"\"", "\n\"\"\"Python\"\"\"")

########2.4.1.7
#create the variables: john, mary, and adam; assign values to the variables. The values must be equal to the numbers of fruit possessed
john = 3
mary = 5
adam = 6

#print the variables on one line, and separate each of them with a comma;
print(john, mary, adam, sep=",")

#now create a new variable named total_apples equal to addition of the three former variables.
#print the value stored in total_apples to the console;
total_apples = (john + mary + adam)
print(total_apples)

#Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples
print("There are", total_apples, "apples all together.")

########2.4.1.9
#complete the program in the editor so that it converts:miles to kilometers;kilometers to miles.
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

########2.4.1.10
#complete the code in order to evaluate the following expression:    3x3 - 2x2 + 3x - 1

x =  0 # variable used as test input to see if the calculation is correct.
# hardcode your test data here
x = float(x)
# write your code here
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1
print("y =", y)

########2.5.1.2
#The code in the editor contains comments. Try to improve it: add or remove comments where you find it appropriate

#this program computes the number of seconds in a given number of hours
a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour
print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye")#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 2 hours.

#########2.6.1.9 Simple input and output

a = float (input("How many cakes have you eaten today?")) # input a float value for variable a here

b = float (input("How many cakes did you eat yesterday?")) # input a float value for variable b here

# output the result of addition here
print ("You have eaten", a + b, " cakes in total")

# output the result of subtraction here
print (a - b, "is the number subratcted")

# output the result of multiplication here
print ("Multiplied together make's ", a * b)

# output the result of division here
print ("and divided is ", a / b)
print("\nThat's all, folks!")

#########2.6.1.10

#Your task is to complete the code in order to evaluate the following expression
x = float(input("Enter value for x: ")) #x is the float value of the usres input
y = 1 / (x + 1/(x + 1 /(x + 1 / x)))  # the mathematical equation when x is as above. The answer will be a float value.
print("y =", y)

#########2.6.1.11

#prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# My code
mins = mins + dura #adding the duration time  in mins to the minute started.
#(mins % 60) number of remaining minutes aftr 1 full hour has passsed.
#(hour % 24) number of remaining hours after 1 full day has passed
hour = hour + mins // 60 # number of 60 mins passd aftre adding duration

#print in the correct format
print(hour % 24, ":", mins % 60, sep= "")