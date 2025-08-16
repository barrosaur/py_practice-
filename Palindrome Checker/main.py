word = input("Enter word: ")

def check_palindrome(word):
  reversed_word = ""

  # starting index which is the last part
  # stopping point (before reaching -1)
  # decrement
  for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

  if reversed_word == word:
    print(f"{word} is a palindrome")
  else:
    print(f"{word} is not a palindrome")

check_palindrome(word)