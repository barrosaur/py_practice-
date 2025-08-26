import login
import sys
import token_logger

def main():
  login_flag = login.login()
  flag = True

  while flag:
    if(login_flag):
      display_menu()
      choice = int(input("Enter choice: "))

      match choice:
        case 1:
          check_something(login_flag)
        case 2:
          token_logger.read_logs(mode="r")
        case 3:
          print("Exiting...")
          login.login()

def display_menu():
  print("=== Menu ===")
  print("[1] - Check something")
  print("[2] - Read logs")
  print("[3] - Exit")

def check_something(token):
  print("Checking something...")
  print(f"Token: {token}")

main()