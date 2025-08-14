import random

print("=== Guess the number ===")
rd_num = random.randint(0, 10)
attempts = 0

while attempts < 3:
  guess_num = int(input("Guess (0-10): "))
  attempts += 1

  if guess_num == rd_num:
    print(f"You guessed it! The number is: {rd_num}")
    break
  elif guess_num < rd_num:
    print("Guess higher...")
  else:
    print("Guess lower...")

if attempts == 3 and guess_num != rd_num:
  print(f"You've ran out of attempts suckah. The number was: {rd_num}")