import string
import random


def generate_password(length):
    """
    Generates a random password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    """6
    The main function that prompts the user for the desired password length
    and generates the password.
    """
    print("Welcome to the Password Generator!")

    while True:
        try:
            password_length = int(input("Enter the desired length of the password (8-32 characters): "))
            if 8 <= password_length <= 32:
                break
            else:
                print("Password length must be between 8 and 32 characters.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    generated_password = generate_password(password_length)
    print(f"Your generated password is: {generated_password}")


if __name__ == "__main__":
    main()