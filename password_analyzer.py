import getpass
import math


COMMON_PASSWORDS = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome"
]


def calculate_entropy(password):
    pool_size = 0

    if any(char.islower() for char in password):
        pool_size += 26

    if any(char.isupper() for char in password):
        pool_size += 26

    if any(char.isdigit() for char in password):
        pool_size += 10

    if any(not char.isalnum() for char in password):
        pool_size += 32

    if pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)

    return entropy


def has_repeated_characters(password):
    if not password:
        return False

    return len(set(password)) <= 3


def check_password(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special character check
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Common password check
    common_password = password.lower() in COMMON_PASSWORDS

    if common_password:
        suggestions.append("Avoid common or easily guessed passwords.")

    # Repeated-character check
    if has_repeated_characters(password):
        suggestions.append(
            "Avoid passwords with very few unique characters."
        )

    # Entropy calculation
    entropy = calculate_entropy(password)

    if entropy < 40:
        entropy_rating = "Low"
    elif entropy < 60:
        entropy_rating = "Moderate"
    else:
        entropy_rating = "Higher"

    # Strength classification
    if common_password:
        strength = "WEAK"
    elif score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    # Results
    print("\n" + "=" * 40)
    print("PASSWORD SECURITY ANALYSIS")
    print("=" * 40)

    print(f"Score: {score}/5")
    print(f"Strength: {strength}")
    print(f"Estimated entropy: {entropy:.2f} bits")
    print(f"Entropy rating: {entropy_rating}")

    if common_password:
        print(" Common password detected")

    if suggestions:
        print("\nSuggestions:")

        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\n✓ No basic improvements needed.")

    print("*" * 40)


def main():
    password = getpass.getpass("Enter a password: ")
    check_password(password)


if __name__ == "__main__":
    main()