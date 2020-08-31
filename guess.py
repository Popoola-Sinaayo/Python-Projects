import random

print("Welcome to our Number Gueesing app")

print("Please guess a number between zero and hundred!")

print("Please note that five number of maximum guesess")

Maximum_Number_of_Guesses = 5

Number = random.randint(0, 100)
Total_number_of_Guesses = 0

while Maximum_Number_of_Guesses != Total_number_of_Guesses:
    Guessed_Number = int(input("Enter The Guessed Number: "))
    if Guessed_Number:
        Total_number_of_Guesses += 1
    if Guessed_Number < 0 or Guessed_Number > 100:
        print("Invalid Input")
    if Guessed_Number >= 0 and Guessed_Number <= 100:
        if Guessed_Number == Number:
            print("You guessed the coreect number")
        elif Guessed_Number < Number:
            print("Guessed number is too small to actual number! Try a larger number")
        elif Guessed_Number > Number:
            print("Guessed number is to large please try a smaller number!")
        elif Guessed_Number < 0 or Guessed_Number > 100:
            print("Invalid Input")
if Maximum_Number_of_Guesses == Total_number_of_Guesses:
    print("The actual number is " + str(Number) + "!")
    print("You have exceeded number of limits please try again!")
