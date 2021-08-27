import art, random

# compare guessed and actual numbers
def compare_number(actual_num, guessed_num):
  if guessed_num > actual_num:
    print("Too high.\nGuess again.")
    return False
  
  elif guessed_num < actual_num:
    print("Too low.\nGuess again.")
    return False

  elif guessed_num == actual_num:
    print(f"You got it! The answer is {actual_num}")
    return True
  
# guessing statements
def ask_to_guess(n):
  for i in range(n):
    print(f"You have {n-i} attempts remaining to guess the number.")
    guessed_num = int(input("Make a guess: "))
    is_guessed = compare_number(actual_num, guessed_num)

    if is_guessed:
      break

  if not is_guessed:
      print("You've run out of guesses, you lose.")

# Print Statements
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking a number between 1 to 100")

#Choosing Random Number
numbers = range(1,101)
actual_num =  random.choice(numbers)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level == 'easy':
  n = 10
  ask_to_guess(n)

elif difficulty_level == 'hard':
  n = 5
  ask_to_guess(n)
