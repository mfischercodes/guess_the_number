''' User guesses between 1 and 50 if outside of range guess again within the range
when they guess wrong ask them if they want to play again or quit
When they get it right you tell them how many attempts it took them.'''

import random

random_number = random.randint(1,50)
print(random_number)

counter = 0
while True:
    try:
        user_input = int(input('Guess a number between 1 and 50: '))
        counter +=1

        if (user_input <1 or user_input > 50):
            counter -=1
            print("You chose a number outside of the range. Please try again.")
        elif user_input < random_number:
            print(f"The number is greater than {user_input}")
        elif user_input > random_number:
            print(f"The number is less than {user_input}")
    except ValueError:
        print("You wrote a string. Please input a number between 1 and 50.")

    if user_input == random_number:
        break
    
print(f"Congratz you guess the number {random_number} in {counter} tries." )


