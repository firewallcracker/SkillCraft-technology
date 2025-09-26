import re

def assess_password_strength(password):
    strength_score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"[0-9]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one number.")

    # Special characters
    if re.search(r"[@$!%*?&#]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one special character (@$!%*?&#).")

    # Strength levels
    if strength_score >= 6:
        strength = "Strong 💪"
    elif strength_score >= 4:
        strength = "Medium ⚡"
    else:
        strength = "Weak ❌"

    return strength, feedback


if __name__ == "__main__":
    pwd = input("Enter a password to check strength: ")
    strength, tips = assess_password_strength(pwd)

    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Suggestions:")
        for t in tips:
            print(f"- {t}")
