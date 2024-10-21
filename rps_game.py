import random
import time

def play_rps():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    while user_choice not in ["rock", "paper", "scissors"]:
      print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
      user_choice = input("Enter your choice: ").lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Well...")
        time.sleep(2)
        print("It's a tie!")
    elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper")):
        print("It seems...")
        time.sleep(2)
        print("You win!")
    else:
        print("It's hard to say..")
        time.sleep(2)
        print("Computer wins!")



if __name__ == "__main__":
  play_rps()
