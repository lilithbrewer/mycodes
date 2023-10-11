# Comments

# Import modules here
from multiprocessing.resource_sharer import stop
import random
from tracemalloc import start
from turtle import st

# Global Varibles
# Program attempts, change varible to the number of rounds
invaild_attempts = 3


# Program Control
while invaild_attempts > 0:
    # Local Varible user_input
    user_input = input("Press 1 for rock, 2 for paper, 3 for scissors:")
    # Validate input to ensure the program does not have invalid input.
    # Return true is a digit is entered, otherwise return to false
    if user_input.isdigit():
       # Only accept 1 digit
      if len(user_input) == 1:
        # Cast to an Integer
        user_input = int(user_input)
        # 1,2,3 numbers only
        # Calculate the computer's value
        # computer value random.randrange(0,3,1)
        computer_value = random.randrange
        # Print computer value for troublehsooting or verify the o/p of the random function
        # print(computer_value)
        print(computer_value)

        if user_input == computer_value:
          # Check if user_unput is 1
          # User wins when  
          # User_input = 1 and computer_value = 3 or computer_value 2
          # Else computer wins   
           if user_input == 1 and computer_value == 3 or user_input == 2:
            print("User Wins") 
        else:
           print("computer Wins")
      else:
          print("Tie Game")
    else: 
        print("Please enter a single digit")
        invaild_attempts = invaild_attempts - 1
else:
        print("Invalid Digit")
        invaild_attempts = invaild_attempts - 1

print("I'm in your walls")