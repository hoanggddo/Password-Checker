# 🔐 Password Strength Checker

This is a simple **GUI-based Password Strength Checker** built with Python's `tkinter` library. The application evaluates the strength of a user's password based on length, character diversity, and whether it appears in a list of commonly used passwords.

## 🚀 Features

- ✅ Checks for uppercase, lowercase, digits, and special characters  
- 📏 Evaluates password length with increasing score for longer passwords  
- ⚠️ Warns if password is found in a list of common passwords (`common.txt`)  
- 📊 Scores password from 0 to 7 and classifies it as:
  - Weak  
  - Okay  
  - Good  
  - Strong  
- 🖥️ GUI built with `tkinter` for ease of use

---

## 🛠️ How It Works

The checker evaluates your password based on:

### 1. Length:
- +1 point for > 8 characters  
- +1 for > 12  
- +1 for > 16  
- +1 for > 20  

### 2. Character Types:
- +1 if it includes more than 1 type  
- +1 if it includes more than 2 types  
- +1 if it includes all 4 types (uppercase, lowercase, digit, special)

**Score: 0–7**  
- 0–3: Weak  
- 4: Okay  
- 5–6: Good  
- 7: Strong

---


## 🖥️ Getting Started

### Prerequisites
- Python 3.x  
- Tkinter (comes pre-installed with Python standard library)

### Running the App

1. Clone or download the repository:
   ```bash
   git clone https://github.com/your-username/PasswordStrengthChecker.git
   cd PasswordStrengthChecker

2.  Make sure common.txt exists in the same directory as checker.py. If not, create one or download a common password list.

3.  Run the app:
    python checker.py


