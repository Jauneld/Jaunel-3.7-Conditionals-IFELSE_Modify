#Jaunel Deans
#October 23, 2023

# Starter Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is "))

if guess == number:# if guess is equal to the value of number
    print("You guessed it!")# if the conditional is true then the console will print "You guessed it!"
else:# if the conditional is false then the computer will run this code 
    print("Nope, that's not it.")#console will print "Nope, try again!"
if guess > 10 or guess < 0:
  print("Bad Luck!")# if the conditional is true then the console will print "Bad Luck!"
else:
  if guess < number:
    print("Too Low!")
  if guess > number:
    print("Too High!")

answer = input("Did you guess the correct number?")#I assigned the variable answer to the input function. The answer can be yes or no. 
if answer == "yes" or answer == "✓" or answer == "y" or answer == "Yes" or answer == "YES": #If one of the conditionals are correct, then it will run the indented code. If it is false it will run the elif statement.  
  print("Well done!") #If the if statement is true the computer will print "Well done!" 
elif answer == "no" or answer == "x" or answer == "n" or answer == "No" or answer == "NO":#If one of the conditionals are correct, then it will run the indented code. If it is false it will run the else statement.  
  print("Nevermind :(")#If the elif statement is true the computer will print "Nevermind :(" 
else: #If none of the conditionals are true, then it will run the else statement.
  print("Invalid Input")#The computer will output "Invaild Input"
  
# End of Starter Code
