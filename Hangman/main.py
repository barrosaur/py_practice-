from wordfreq import top_n_list as word_source
import random
import drawHangman

def generate_random_word():
  common_words = word_source("en", 5000)
  common_words_list = list(common_words)
  random_common_word = random.choice(common_words_list)

  return random_common_word

def draw_hangman(attempts):
  match(attempts):
    case 5:
      drawHangman.draw_hangman_1()
    case 4:
      drawHangman.draw_hangman_2()
    case 3:
      drawHangman.draw_hangman_3()
    case 2:
      drawHangman.draw_hangman_4()
    case 1:
      drawHangman.draw_hangman_5()  

# generates word for the current game and sets it
current_word = generate_random_word()

# hidden word with underscores
hidden_word = ["_"] * len(current_word)

# reveal 1 or 2 random letters at the start of the game
start_reveal = random.randint(1, 2)
# list of indexes in the word you wanna reveal
revealed_position = random.sample(range(len(current_word)), start_reveal)

for pos in revealed_position:
  # the current word gets converted into _ 
  # to hide it
  hidden_word[pos] = current_word[pos]

# keep track of user attempts
attempts = 5

# start of game
print("=== Welcome to Hangman ===")
print("You have 5 attempts to guess the certain word.")
print("Good luck!")

# shows initial word with underscores for guesses
print("\nThe Word is: ", " ".join(hidden_word) +"\n")

while attempts > 0:
  print(f"\nAttempts: {attempts} left")

  # easier for comparing strings
  guess = input("Guess: ").lower()

  if guess == current_word:
    print("✅ You guessed the word!")
    break
  else:
    attempts -= 1

    if attempts == 0:
      print(f"❌ Out of attempts: {attempts}/5")
      print(f"The word is: {current_word}")
      break

    # draws each hangman stage
    print("\nOops. Try Again")
    draw_hangman(attempts)

    # goes thru each index with their corresponding characters
    # in the hidden_word
    # collects all indexes where the ch is still an _
    unrevealed_pos = [i for i, ch in enumerate(hidden_word) if ch == "_"]

    # checks if there are still hidden letters
    if unrevealed_pos:
      # randomized character reveal
      pos = random.choice(unrevealed_pos)
      hidden_word[pos] = current_word[pos]
    print(" ".join(hidden_word))

    # if there are no more underscores
    # that means the word is revealed
    # you lost
    if "_" not in hidden_word:
      print(f"The word is: {current_word}")
      break