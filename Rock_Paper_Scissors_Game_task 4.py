import random


def get_user_choice():
    """
    Prompts the user to choose rock, paper, or scissors.

    Returns:
        str: The user's choice.
    """
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")


def get_computer_choice():
    """
    Generates a random choice (rock, paper, or scissors) for the computer.

    Returns:
        str: The computer's choice.
    """
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the user's and computer's choices.

    Args:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.

    Returns:
        str: The result of the game (win, lose, or tie).
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose."


def play_game():
    """
    Runs the rock-paper-scissors game.
    """
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}, the computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose.":
            computer_score += 1

        print(f"Current score: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            break


if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    play_game()