def check_password_strength(password):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    score = 0

    # Conditions
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)

    # Scoring (20 points each)
    if has_length:
        score += 20
    if has_upper:
        score += 20
    if has_lower:
        score += 20
    if has_digit:
        score += 20
    if has_special:
        score += 20

    # Rating
    if score < 40:
        rating = "Weak"
    elif score < 80:
        rating = "Fair"
    else:
        rating = "Strong"

    return score, rating

score, rating = check_password_strength("Password1")
print(f"Score: {score}/100 | Rating: {rating}")

# CODE #2

# def check_password_strength(password):
#     if not isinstance(password, str):
#         raise TypeError("Password must be a string")
    
#     score = 0
#     feedback = []
#     special_chars = set("!@#$%^&*()")
    
#     if len(password) >= 8:
#         score += 20
#     else:
#         feedback.append("Use at least 8 characters")
    
#     if any(c.isupper() for c in password):
#         score += 20
#     else:
#         feedback.append("Add at least one uppercase letter")
    
#     if any(c.islower() for c in password):
#         score += 20
#     else:
#         feedback.append("Add at least one lowercase letter")
    
#     if any(c.isdigit() for c in password):
#         score += 20
#     else:
#         feedback.append("Add at least one number")
    
#     if any(c in special_chars for c in password):
#         score += 20
#     else:
#         feedback.append("Add a special character like ! @ # $")
    
#     rating = "Weak" if score < 40 else "Fair" if score < 80 else "Strong"
    
#     if not feedback:
#         feedback.append("Great password!")
    
#     return score, rating, feedback

# score, rating, tips = check_password_strength("Password1!")
# print(f"Score: {score}/100 | Rating: {rating}")
# for tip in tips:
#     print(f"  → {tip}")