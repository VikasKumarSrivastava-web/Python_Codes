from random import *

not_game_end= True
print('Welcome to the number guessing game!')
print('I am thinking of a number between 1 to 100')
user_choice = input("Choose a difficulty. Type 'easy' or 'hard' : ")
random_number= randint(1,100)
print(random_number)

if user_choice =='easy':
  attempt=10
elif user_choice =='hard':
  attempt=5
else:
  print('invalid entry')

def wrong_guess(attempt):
  print(f"You have {attempt} attempts remaining to guess the number.")
  print("guess again")

print(f"You have {attempt} attempts remaining to guess the number.")
while not_game_end:
  guess=int(input("Make a guess : "))
  if guess != random_number:
    if attempt > 1:
      if guess < random_number:
        attempt = attempt - 1
        print("Too low")
        wrong_guess(attempt)  
      else:
        attempt = attempt - 1
        print("Too High")
        wrong_guess(attempt)
    else:
      print("You have run out of guess")
      print("You Lose.")
      not_game_end = False
  else:
    print(f"You Got it. The answer was {random_number}")
    not_game_end=False