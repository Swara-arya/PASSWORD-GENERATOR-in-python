import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Characters to choose from
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = upper + lower + digits + symbols

    # Ensure at least one of each character type is included
    password = random.choice(upper) + random.choice(lower) + random.choice(digits) + random.choice(symbols)

    # Fill the rest with random choices
    password += ''.join(random.choices(all_chars, k=length - 4))

    # Shuffle the password to avoid predictable patterns
    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)

# Get user input
try:
    user_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(user_length)
    print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")
