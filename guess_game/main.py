import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
  attempts = 10
else:
  attempts = 5

def guess_number():
  global attempts
  print(f"You have {attempts} attempts remaining to guess the number. ")
  user_guess = int(input("Make a guess: "))
  if user_guess == number:
    print(f"You got it! The answer was {number}.")
    return True
  elif user_guess > number:
    print("Too high.")
    attempts -= 1
    if attempts > 0:
      print("Guess again.")
    return False
  elif user_guess < number:
    print("Too low.")
    attempts -= 1
    if attempts > 0:
      print("Guess again.")
    return False

while attempts > 0:
  if guess_number():
    break
  else:
    continue
    
if attempts == 0:
  print("You've run out of guesses, you lose.")