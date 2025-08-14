import random

print("\nRock✊ Paper🤚 Scissors✌️\n")
score_comp = 0
score_player = 0
options = ["rock", "paper", "scissors"]

while score_comp < 3 and score_player < 3:
  comp_choice = random.choice(options)
  player_choice = input("Your turn: ")
  print(f"Computer's choice: {comp_choice}")

  same_condition = (comp_choice == "rock" and player_choice == "rock") or\
                   (comp_choice == "paper" and player_choice == "paper") or\
                   (comp_choice == "scissors" and player_choice == "scissors")

  # continue winning logic
  player_win_condition = (player_choice == "rock" and comp_choice == "scissors") or\
                         (player_choice == "scissors" and comp_choice == "paper") or\
                         (player_choice == "paper" and comp_choice == "rock")
  if player_win_condition:
    print("\nPlayer scores!\n")
    score_player += 1
  elif same_condition:
    print("\nTie\n")
  else:
    print("\nComputer scores!\n")
    score_comp += 1

print(f"\nPlayer Score: {score_player}")
print(f"Computer Score: {score_comp}\n")
if score_player == 3:
  print("\nPlayer wins!\n")
elif score_comp == 3:
  print("\nComputer wins!\n")
else:
  print("\nIt's a Tie!\n")