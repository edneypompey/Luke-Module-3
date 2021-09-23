###### Luke Edney SIMR 20 001 - Last updated Thurs 23rd Sep 2021 - go to line 236 for latest work

###Tues 21 Sep 

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

##### 3.2.1.6

import time

for timer in range(1, 6): #for loop that counts from one to five.
    print(timer," Mississippi") #prints the timer variable and missippi in increments of 1.
    time.sleep(1) #sleep for 1 second, then go back to the for statement4

print("Ready or not, here I come!") #once for loop has completed run this string

#####3.2.1.9

#Design a program that uses a while loop and continuously asks the user to enter
#a word unless the user enters "chupacabra" as the secret exit word
# in which case the message "You've successfully left the loop." 
#should be printed to the screen, and the loop should terminate.

##### I DO NOT UNDERSTAND WHATS HAPPENING HERE###### MODEL SOLUTION BELOW ########

while True:
    word = input("Enter 'chupacabra' leave the loop: ")
    if word == "chupacabra": #if the word input by the user is true then break imediately
        break 
print("You've successfully left the loop!") #Print once exiting the loop

#####3.2.1.10

#you must design a vowel eater! Write a program that uses:
#a for loop;the concept of conditional execution (if-elif-else)
#the continue statement.
#Your program must: ask the user to enter a word;
#use user_word = user_word.upper() to convert the word entered by the user to upper case;
#use conditional execution and the continue statement to "eat" the following 
#vowels A, E, I, O, U from the inputted word;
#print the uneaten letters to the screen, each one of them on a separate lin

userword =input("Enter a word: ") #Prompt the user to enter a word
userword = userword.upper() #change the variable into uppercase

for letter in userword:
        if letter == "A": #if word includes A do nothing and continue
            continue
        elif letter == "E": #if word includes E do nothing and continue
             continue
        elif letter == "I": #if word includes I do nothing and continue
             continue
        elif letter == "O": #if word includes O do nothing and continue
             continue
        elif letter == "U": #if word includes U do nothing and continue
            continue
        else:
            print(letter) #print all other letters

###3.2.1.11

#you must redesign the (ugly) vowel eater from the previous lab
#Write a program that uses:
#a for loop;
#the concept of conditional execution (if-elif-else)
#the continue statement

#Your program must:
#ask the user to enter a word;
#use user_word = user_word.upper()
#use conditional execution and the continue statement to "eat" the following vowels 
#A, E, I, O, U from the inputted word;
#assign the uneaten letters to the word_without_vowels variable
#and print the variable to the screen.

wordWithoutVowels = "" #an empty string

userword =input("Enter a word: ") #Prompt the user to enter a word
userword = userword.upper() #change the variable into uppercase

for letter in userword:
        if letter == "A": #if word includes A do nothing and continue
            continue
        elif letter == "E": #if word includes E do nothing and continue
             continue
        elif letter == "I": #if word includes I do nothing and continue
             continue
        elif letter == "O": #if word includes O do nothing and continue
             continue
        elif letter == "U": #if word includes U do nothing and continue
            continue
        else:
            wordWithoutVowels = wordWithoutVowels + letter 
        #add letters from user input into the empty variable, execpt the vowels
            
print(wordWithoutVowels)

#######3.2.1.14

#Your task is to write a program which reads the number of blocks the builders have, 
#and outputs the height of the pyramid that can be built using these blocks.

##### I DO NOT UNDERSTAND WHATS HAPPENING HERE###### MODEL SOLUTION BELOW ########

blocks = int(input("Enter the number of blocks: "))

height = 0 #create height variable
layer = 1 #create layer variable
while layer <= blocks: 
    height += 1
    blocks -= layer
    layer += 1

print("The height of the pyramid:", height) #when the while loop has ceased print this

#####3.2.1.15

### DID NOT UNDERSTAND THE QUESTION ###### MODEL SOLUTION BELOW ########

c0 = int(input("Enter c0: ")) 

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0: #test if the number is even, where c0 is the variable.
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")

##### Thurs 23rd Sep

##### 3.4.1.6 the basics of lists

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
# Step 2: write a line of code that removes the last element from the list.
# Step 3: write a line of code that prints the length of the existing list.

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

user_input = int(input("Please enter a number: ")) # prompts user to enter a number
hat_list[2] = user_input # Copying value of the user input into indxex 2 (middle value)

del hat_list[4] # Removing index 4 element from the list.

print("List Length: ", len(hat_list)) #print the length of the lists' elements.

#### 3.4.1.13

# step 1: create an empty list named beatles;
beatles = []
print("Step 1:", beatles)

#step 2: use the append() method to add the following members of the band to the list: 
#John Lennon, Paul McCartney, and George Harrison;
beatles.append('John Lennon',)# add John to the list
beatles.append('Paul McCartney') # add Pual to the list
beatles.append('George Harrison') # add george to the list
print("Step 2:", beatles)

# step 3: use the for loop and the append() method to prompt the user 
# to add the following members of the band to the list: Stu Sutcliffe, and Pete Best
for new_member in range(2): #create variable new_member and loop it 2 times before exiting loop
    user_new_member = input("Enter another member: ") #prompt user to enter a new name and assign it to the variable user_new_variable
    beatles.append(user_new_member) # appends the user input to the end of the the list
print("Step 3:", beatles)

# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles[3]  # Removing Stu Sutcliffe from the list.
print("Step 4:", beatles)

#step 5: use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, 'Ringo Starr') # add the strinf Ringo Starr into index 0
print("Step 5:", beatles)

####3.6.1.9

#write a program which removes all the number repetitions from the list. 
#have a list in which all the numbers appear not more than once.
#you can improve the code and add a part that can carry out a conversation with the user 
#and obtain all the data from her/him.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] #original list

new_list = my_list[:] #make a copy of my_list
new_list.sort() # sort the list to make it esy for the user to understand
print(new_list) # show list to the user
remove_value = int(input("Are there any duplicate numbers? If so type the number below: ")) #prompt user for duplicate values
print("removing ",remove_value)#print value to be removed and the list for user

for i in new_list: # loop that when the user value is in the new_list, remove it 
    new_list.remove(remove_value) #remove the value input by the user
    print(new_list) # re-print list for user and get them to try another dupicate
    remove_value = int(input("Any more, If so type the number below or type 007: ")) #re-prompt the user
    print("removing ",remove_value)#print value to be removed and the list for user
else:
    print("Well done , this is the  list with unique elements only:\n", new_list) #conratulate the user