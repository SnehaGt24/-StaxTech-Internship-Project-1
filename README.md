## Password Generator Project using Python
A secure and customizable password generator built with Python.

## Features

- Generates strong, random passwords
- Customizable password length (minimum 4 characters)
- Options to include/exclude:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*, etc.)
- Ensures at least one character from each selected character set
- User-friendly command-line interface

## Requirements

- Python 3.x

## Usage

1. Run the script:
   ```bash
   python PasswordGenerator.py
   
2. Follow the prompts to configure your password:
   - Enter desired password length (default: 12)
   - Choose which character types to include (Y/n)

3.  Your secure password will be generated and displayed

## Security Notes

  - Passwords are generated using Python's secure random number generator
  - The script ensures at least one character from each selected character set
  - For maximum security, use longer passwords (16+ characters) with all character types enabled
