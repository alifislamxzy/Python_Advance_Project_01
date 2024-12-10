import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_characters=True):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special_characters else ''
    
    # Combine all character pools
    all_characters = lowercase + uppercase + digits + special
    
    if not all_characters:
        raise ValueError("At least one type of character must be selected!")
    
    # Ensure the password includes at least one character from each selected pool
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(digits))
    if use_special_characters:
        password.append(random.choice(special))
    password.append(random.choice(lowercase))
    
    # Fill the rest of the password length with random choices
    while len(password) < length:
        password.append(random.choice(all_characters))
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

# User inputs for customization
try:
    length = int(input("Enter the desired password length (minimum 4): "))
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_special_characters = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_characters)
    print("\nGenerated Password:", password)
except ValueError as e:
    print("Error:", e)
