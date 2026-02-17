import random
random_number : int = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 20.")    
print("You have 3 attempts to guess the number.")
attempts : int = 0

while attempts < 3:
    guess : int = int(input("Make a guess: "))
    difference : int = guess - random_number
    # print (f"Your guess is {difference} away from the number.")
    # print(f"guess is {guess} and random number is {random_number}")
    attempts += 1
    if guess < 1 or guess > 20:
        print(f"You lose your 1 attempt. you have {3 - attempts} attempts left. Please enter a valid number between 1 and 20.")
        continue
    
    
    if difference == 0:
        print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts!")
        break
    elif difference < 0:
        if difference <= 3:
            print("Your guess is low, but you're getting warmer!")
        else:
            print("Your guess is too low. Try again!")
    else:
        if difference <= 3:
            print("Your guess is high, but you're getting warmer!")
        else:
            print("Your guess is too high. Try again!")
else:    print(f"Sorry, you've used all 3 attempts. The number was {random_number}.")       
