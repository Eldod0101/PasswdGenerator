import random

# Define character sets
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_chars = '!@#$%^&*'

# Combine all character sets
all_chars = lowercase + uppercase + numbers + special_chars

# Set to store generated passwords
generated_passwords = set()

def generate_password():
    while True:
        # Start with one character from each category
        pwd = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(numbers),
            random.choice(special_chars)
        ]
        # Add random characters until the password is 20 characters long
        while len(pwd) < 20:
            next_char = random.choice(all_chars)
            # Check for more than two identical characters in a row
            if len(pwd) >= 1 and pwd[-1] == next_char:
                # If the last character is the same, check if there is another identical before
                if len(pwd) >= 2 and pwd[-2] == next_char:
                    continue  # Skip adding this character
            pwd.append(next_char)
        # Convert list to string
        password = ''.join(pwd)
        # Check if password meets the requirements
        # At least 4 of the following categories are present
        has_lower = any(c in lowercase for c in password)
        has_upper = any(c in uppercase for c in password)
        has_number = any(c in numbers for c in password)
        has_special = any(c in special_chars for c in password)
        # At least one from each category
        if has_lower and has_upper and has_number and has_special:
            return password

def generate_unique_passwords(n):
    passwords = []
    while len(passwords) < n:
        pwd = generate_password()
        if pwd not in generated_passwords:
            generated_passwords.add(pwd)
            passwords.append(pwd)
    return passwords

# Example usage: Generate 5 unique passwords
unique_passwords = generate_unique_passwords(5)
for pwd in unique_passwords:
    print(pwd)