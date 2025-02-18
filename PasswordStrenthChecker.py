import re
import os

def load_common_passwords(file_path='common_passwords.txt'):
    """Load a list of common passwords from a file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip().lower() for line in file]
    except FileNotFoundError:
        print(f"Warning: Common passwords file not found at {file_path}")
        return []

def is_common_password(password, common_list):
    """Check if password exists in common passwords list."""
    return password.lower() in common_list

def calculate_strength(password, common_list):
    """Calculate password strength score (0-100)."""
    score = 0
    
    # Length check (12-64 characters recommended by NIST)
    if len(password) >= 12:
        score += 25
    elif 8 <= len(password) < 12:
        score += 10
    else:
        return 0  # Too short
    
    # Character variety checks
    checks = {
        'lower': r'[a-z]',
        'upper': r'[A-Z]',
        'digit': r'\d',
        'special': r'[^A-Za-z0-9]'
    }
    
    for value in checks.values():
        if re.search(value, password):
            score += 12.5  # Max 50 points (4 categories)
    
    # Deduct points for common passwords
    if is_common_password(password, common_list):
        score = max(score - 50, 0)
    
    return min(100, score)

def get_feedback(score):
    """Generate human-readable feedback."""
    if score >= 75:
        return "Strong", "✅ Good password security"
    elif score >= 50:
        return "Moderate", "⚠️ Could be improved"
    return "Weak", "❌ Immediately change this password"

def main():
    common_passwords = load_common_passwords()
    
    print("Password Strength Checker")
    print("-"*30)
    password = input("Enter password to check: ").strip()
    
    strength_score = calculate_strength(password, common_passwords)
    rating, feedback = get_feedback(strength_score)
    
    print(f"\nStrength Rating: {rating} ({strength_score}/100)")
    print(f"Feedback: {feedback}")
    
    if is_common_password(password, common_passwords):
        print("\nWarning: This password appears in common breach lists!")

if __name__ == "__main__":
    main()