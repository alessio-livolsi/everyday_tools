# python
import random
import string


def generate_password(length):
    """
    Generate a secure random password with the following rules:
    - Minimum length: 8 characters
    - Maximum length: 128 characters
    - Must contain at least one uppercase letter, one digit, and one special character.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    if length > 128:
        raise ValueError("Password length must be no more than 128 characters.")

    # define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # ensure required complexity
    password = [
        # at least one uppercase letter
        random.choice(uppercase),
        # at least one digit
        random.choice(digits),
        # at least one special character
        random.choice(symbols),
    ]

    # fill the remaining characters from a mixed pool
    all_characters = lowercase + uppercase + digits + symbols
    while len(password) < length:
        password.append(random.choice(all_characters))

    # shuffle to avoid predictable patterns
    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print("welcome to the password generator!")
    while True:
        try:
            length = int(
                input("enter the desired password length (minimum 8, maximum 128): ")
            )
            password = generate_password(length)
            print(f"your generated password is: {password}")
            break
        except ValueError as e:
            print(e)
