import generateToken
import json
import sys
import token_logger

with open("users.json", "r") as file:
  user_data = json.load(file)

def login(): 
  username = input("Enter username: ")
  password = input("Enter password: ")
  role = input("Enter role (admin or normie): ")

  for user in user_data["users"]:
    condition = username == user["username"] and password == user["password"] and \
                role == user["role"]
    
    if(condition):
      print("User found!")

      custom_token = generateToken.generate_token()
      print(f"Custom token: {custom_token}")
      token_logger.write_to_logs(token=custom_token)

      return custom_token
  
  print("User not found\n")
  print("Exiting...")
  sys.exit(0)