import re

def check_strength(pwd):
    score = 0
    notes = []

#length check
    if len(pwd) >= 12:
        score += 5
        notes.append("Length is excellent (12+)")
    elif len(pwd) >= 8:
        score += 3
        notes.append("Length is good (8–11)")
    else:
        notes.append("Too short (less than 8)")

#character type checks
    if re.search(r"[A-Z]", pwd):
        score += 2
        notes.append("Has uppercase letter")
    if re.search(r"[a-z]", pwd):
        score += 2
        notes.append("Has lowercase letter")
    if re.search(r"\d", pwd):
        score += 2
        notes.append("Has a number")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 2
        notes.append("Has special character")

#simple repetition check
    if re.search(r"(.)\1\1", pwd):
        score -= 3
        notes.append("Avoid repeating the same character 3+ times")

#decide strength
    if score >= 10:
        rating = "Very Strong"
    elif score >= 8:
        rating = "Strong"
    elif score >= 6:
        rating = "Good"
    elif score >= 4:
        rating = "Weak"
    else:
        rating = "Very Weak"

    return rating, notes

if __name__ == "__main__":
    password = input("Enter a password to check: ").strip()
    if not password:
        print("Password cannot be empty.")
    else:
        level, tips = check_strength(password)
        print("\nStrength:", level)
        print("Details:")
        for t in tips:
            print(" -", t)
