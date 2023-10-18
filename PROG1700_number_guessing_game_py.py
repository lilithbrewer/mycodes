'''Author: Vanessa Brewer
Student ID: <W0487885>
Course: PROG1700
Date: 10/17/23
Repository: GitHub ( https://github.com/vanessabrewer/wwwroot#readme )
Licence: Creative Commons
Version: 1.0 '''


import random

#define the range and the max_attempts
lower_bound = 1
upper_bound = 10
max_attempts = 5

#generate a secert random number
secret_number =
random.randint(lower_bound, upper_bound)

name = input("What's your name?")
print('Hey,', name, 'This is a guessing game. I will pick a number between 1 and 10, and you have to guess it. you have 5 attempts. bet you cant guess it though but if you do congrats I guess.')

#players guess
def get_guess(atempts) :
  while True:
   try: 
         guess = int(input (f"What is your guess, {lower_bound} - {upper_bound}? ")) 
         upper_bound: return guess
  
  else:
     print("Invaild input. Enter a number within the specified range.")
     Except ValueError
     print("Invalid input. Enter a valid number.")
     #exit game after 3 invalid inputs.
     attempts += 1
     if atempts > 3:
        print("Thats too many inncorrect guesses. I knew you wouldnt be able to guess it.")
        exit ()

    # Validate the guess
def check_guess(guess, secert_number):
 if guess == secret_number:
     return "Correct"

 elif guess < secret_number:
    return "Your guess is too low. Try again."
 
 else:
    return "Your guess is too high. Try again or give up you cant win."
 
 #track the number of attempts and detect if the game is over
 def play_game():
    attempts = 0
    won = False

    while max_attempts < max_attempts:
       Attempts += 1
       guess = get_guess(attempts)
       result = check_guess, (guess, secert_number)

    if result == "Correct":
       print(f"HEY WHAT..I mean congrats you guessed the number..{secert_number in attempts} attempts")
       won = True

       break

    else:
        print(f"{result}. Try again..") 

        if not won: 
           print(f"You guessed the number in 3 tries. The secert number is {secert_number}.")
        if __name__ == " __main__": 
           print("Welcome to this Number Guessing Game I guess I bet you wont be able to guess it.")
           play_game() 





