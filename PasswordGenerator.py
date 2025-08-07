import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    character_sets = []
    
    if uppercase:
        character_sets.append(string.ascii_uppercase)
    if lowercase:
        character_sets.append(string.ascii_lowercase)
    if numbers:
        character_sets.append(string.digits)
    if special_chars:
        character_sets.append(string.punctuation)
    
    if not character_sets:
        raise ValueError("At least one character set must be selected")
    
    password = []
    for charset in character_sets:
        password.append(random.choice(charset))
    
    all_chars = ''.join(character_sets)
    password.extend(random.choices(all_chars, k=length - len(password)))
    random.shuffle(password)
    
    return ''.join(password)

def get_user_input():
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        if length < 4:
            print("Password length too short. Setting to minimum of 4.")
            length = 4
        
        uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
        lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
        numbers = input("Include numbers? (Y/n): ").lower() != 'n'
        special_chars = input("Include special characters? (Y/n): ").lower() != 'n'
        
        return length, uppercase, lowercase, numbers, special_chars
    except ValueError:
        print("Invalid input. Using default values.")
        return 12, True, True, True, True

def main():
    print("=== Password Generator ===")
    print("Configure your password requirements:")
    
    length, uppercase, lowercase, numbers, special_chars = get_user_input()
    
    try:
        password = generate_password(length, uppercase, lowercase, numbers, special_chars)
        print("\nGenerated Password:", password)
        print("Password length:", len(password))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()