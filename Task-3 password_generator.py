import random
import string

# User Inputs
length = int(input("Enter password length (minimum 6): "))

if length < 6:
    print("Password length too short! Setting length to 6.")
    length = 6

print("\nChoose password requirements:")
use_upper = input("Include uppercase letters? (yes/no): ").lower()
use_numbers = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include special characters? (yes/no): ").lower()

# Base characters
characters = string.ascii_lowercase

if use_upper == "yes":
    characters += string.ascii_uppercase

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

# Password generation
password = ""

for i in range(length):
    password += random.choice(characters)

# Password Strength Check
strength = "Weak"

if length >= 10 and use_upper == "yes" and use_numbers == "yes" and use_symbols == "yes":
    strength = "Strong"
elif length >= 8:
    strength = "Medium"

print("\n----------------------------------------")
print("Generated Password:", password)
print("Password Strength:", strength)
print("----------------------------------------")

# Security Tips
print("""
PASSWORD SECURITY TIPS:
- Do not share your password with anyone
- Use different passwords for different websites
- Change passwords regularly
- Avoid using your name or date of birth
""")


