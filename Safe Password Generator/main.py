import string
import secrets

min_length = 12
max_length = 16
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbols = string.punctuation

password = ""

while len(password) < 12 or len(password) > 16:
  characters = lowercase + uppercase + symbols
  password += secrets.choice(characters)
  
print(f"Password: {password}")
print(f"Password length: {len(password)}")