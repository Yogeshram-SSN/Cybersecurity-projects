import re
import os

def check_password_strength(password):
    length_check = len(password) >= 8
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_lowercase = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[\W_]', password) is not None

    score = 0
    score += 2 if length_check else 0
    score += 2 if has_uppercase else 0
    score += 2 if has_lowercase else 0
    score += 2 if has_digit else 0
    score += 2 if has_special else 0

    feedback = []
    if not length_check:
        feedback.append("Password must be at least 8 characters long.")
    if not has_uppercase:
        feedback.append("Password must include at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password must include at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password must include at least one digit.")
    if not has_special:
        feedback.append("Password must include at least one special character.")
    
    return score, feedback

def estimate_cracking_difficulty(password):
    """
    Provides an estimate of how easy or hard it is to crack the password.
    """
    length = len(password)
    diversity = len(set(password))  
    entropy = length * diversity

    if entropy < 30:
        return "Very Easy (crackable in seconds)"
    elif entropy < 50:
        return "Easy (crackable in minutes)"
    elif entropy < 70:
        return "Moderate (crackable in hours)"
    elif entropy < 90:
        return "Strong (crackable in days or weeks)"
    else:
        return "Very Strong (crackable in years or longer)"

def process_password_file(file_path):
    """
    Processes a file containing passwords and checks each password for validity.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    try:
        with open(file_path, 'r') as file:
            print(f"Processing passwords from '{file_path}'...\n")
            for password in file:
                password = password.strip()  
                if not password:
                    continue  

                score, feedback = check_password_strength(password)
                cracking_difficulty = estimate_cracking_difficulty(password)

                if score == 10:
                    print(f"Valid Password: {password} | Strength: {cracking_difficulty}")
                else:
                    print(f"Invalid Password: {password}")
                    print(f"  Strength Score: {score}/10")
                    print(f"  Feedback: {'; '.join(feedback)}")
                    print(f"  Cracking Difficulty: {cracking_difficulty}")
                print("-" * 50)
    except Exception as e:
        print(f"Error processing file: {e}")


file_path = r'e:\Cybersecurity\Projects py\passwords.txt'  
process_password_file(file_path)
