# 🔐 Password Strength Analyzer

A beginner-friendly Python cybersecurity project that analyzes password strength using multiple security criteria.

## 📌 Project Overview

The Password Strength Analyzer evaluates a password based on:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Common password detection
* Character diversity
* Estimated entropy

The program assigns a score out of 5 and classifies the password as **Weak**, **Medium**, or **Strong**.

It also provides suggestions to help improve password security.

## 🛠️ Technologies Used

* Python 3
* `getpass`
* `math`
* Python Standard Library

## 🔐 Cybersecurity Concepts

This project demonstrates basic concepts related to:

* Password security
* Password complexity
* Common password risks
* Brute-force resistance
* Entropy
* Input validation
* Defensive cybersecurity

## ⚙️ Features

### 1. Password Length Check

Checks whether the password contains at least 12 characters.

### 2. Character Diversity

Checks for:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

### 3. Common Password Detection

Checks the password against a small educational list of commonly used passwords.

### 4. Password Scoring

The password receives one point for each basic security requirement it satisfies.

### 5. Strength Classification

The program classifies the password as:

* **WEAK**
* **MEDIUM**
* **STRONG**

### 6. Security Suggestions

The program identifies missing security characteristics and provides improvement suggestions.

### 7. Entropy Estimation

The program provides a simplified estimate of password entropy based on password length and character categories.

## 🚀 How to Run

Make sure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/password-strength-analyzer.git
```

Move into the project directory:

```bash
cd password-strength-analyzer
```

Run the program:

```bash
python password_analyzer.py
```

## 📂 Project Structure

```text
password-strength-analyzer/
│
├── password_analyzer.py
├── README.md
└── .gitignore
```

## 🧪 Example

```text
Enter a password:

========================================
PASSWORD SECURITY ANALYSIS
========================================
Score: 5/5
Strength: STRONG
Estimated entropy: 65.43 bits
Entropy rating: Higher

✓ No basic improvements needed.
========================================
```

*The exact entropy value depends on the password entered.*

## ⚠️ Disclaimer

This project is intended for **educational and defensive cybersecurity purposes**.

The analyzer provides a basic assessment and does not guarantee that a password is secure against all real-world attacks.

The common-password list is intentionally small and is provided only for learning purposes.

## 🔮 Future Improvements

Possible future versions could include:

* Larger common-password datasets
* Better repeated-pattern detection
* More advanced password analysis
* Graphical user interface
* Web-based interface
* Password-strength visualization
* Unit tests
* Improved password security recommendations

## 👨‍💻 Author

**Thushar C. Suvarna**

Cybersecurity Student | Python Learner | Aspiring Cybersecurity Professional
