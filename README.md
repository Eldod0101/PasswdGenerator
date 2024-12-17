Password Generator Script
Introduction

A Python script to generate strong, unique passwords that meet specific security criteria. The script ensures that each password is secure and unique, making it suitable for various applications requiring robust password generation.
Features

    Generates passwords with a minimum length of 20 characters.

    Ensures each password contains at least one lowercase letter, one uppercase letter, one number, and one special character.

    Prevents more than two identical characters in a row.

    Generates a specified number of unique passwords.

Installation

To use this script, you need Python 3.x installed on your system. No additional dependencies are required.
Usage

    Running the Script: Save the script to a file, for example, password_generator.py, and run it using the command:
    bash
    Copy

    python password_generator.py

    Generating Passwords: The script includes an example that generates 5 unique passwords. You can modify the generate_unique_passwords(n) function call to generate a different number of passwords.

How it Works

    Password Generation:

        The generate_password() function creates a password by selecting one character from each category (lowercase, uppercase, numbers, special characters).

        Additional characters are randomly selected from the combined character set to reach a length of 20 characters.

        The function ensures no more than two identical characters are consecutive.

    Ensuring Uniqueness:

        The generate_unique_passwords(n) function generates n unique passwords by storing them in a set, ensuring no duplicates are produced.

Requirements

    Python 3.x

Contributing

While this is a simple script, contributions are welcome. Please open an issue or submit a pull request if you have suggestions or improvements.
License

This project is licensed under the MIT License - see the LICENSE file for details.
