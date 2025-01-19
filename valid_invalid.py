import re
import random
import string

def validate_password(password):
    
    score = 0

    
    length = len(password)
    if length >= 8:
        score += 2  
    if length >= 12:
        score += 2  

    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if has_upper:
        score += 2
    if has_lower:
        score += 2
    if has_digit:
        score += 1
    if has_special:
        score += 2

    
    entropy = length * (has_upper + has_lower + has_digit + has_special)
    cracking_time = estimate_cracking_time(entropy)

    return score, cracking_time

def estimate_cracking_time(entropy):
    """
    Rough estimate of cracking time based on entropy:
    - Less than 20: Very weak
    - 20-40: Weak
    - 40-60: Moderate
    - 60-80: Strong
    - Above 80: Very strong
    """
    if entropy < 20:
        return "Very Easy (less than 1 second)"
    elif entropy < 40:
        return "Easy (a few seconds)"
    elif entropy < 60:
        return "Moderate (minutes to hours)"
    elif entropy < 80:
        return "Strong (days to months)"
    else:
        return "Very Strong (years or longer)"

def suggest_alternative_passwords(password):
    
    suggestions = []
    for _ in range(3):
        alt_password = ''.join(random.choices(
            string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?", k=max(len(password), 12)
        ))
        suggestions.append(alt_password)
    return suggestions


password = input("Input your password: ")
score, cracking_time = validate_password(password)

print(f"\nPassword strength score: {score}/10")
print(f"Estimated difficulty to crack: {cracking_time}")

if score < 6:
    print("\nYour password is weak. Consider the following alternatives:")
    suggestions = suggest_alternative_passwords(password)
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")
else:
    print("Your password is strong!")
