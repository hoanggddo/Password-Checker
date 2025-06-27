# 🔐 Password Strength Checker

A simple yet effective **GUI-based Password Strength Checker** built with Python's `tkinter` library. This application helps users evaluate the strength of their passwords by analyzing length, character diversity, and checking against a common password list.

---

## 🚀 Features

- ✅ Detects uppercase, lowercase, digits, and special characters  
- 📏 Password length evaluation with progressive scoring for longer passwords  
- ⚠️ Checks password against a list of commonly used passwords (`common.txt`) and warns if found  
- 📊 Scores passwords from 0 to 7, categorizing them as Weak, Okay, Good, or Strong  
- 🖥️ User-friendly graphical interface using `tkinter` for easy interaction  
- 🔄 Real-time strength updates as user types (if implemented)  
- 📁 Easily customizable common password list

---

## 🛠️ How It Works

The password checker scores your password based on two main factors:

### 1. Length Criteria

| Length             | Points Awarded |
|--------------------|----------------|
| More than 8 chars  | +1             |
| More than 12 chars | +1             |
| More than 16 chars | +1             |
| More than 20 chars | +1             |

### 2. Character Variety

| Criterion                      | Points Awarded |
|-------------------------------|----------------|
| Contains more than 1 type      | +1             |
| Contains more than 2 types     | +1             |
| Contains all 4 types (upper, lower, digit, special) | +1             |

### Scoring and Classification

| Score | Classification |
|-------|----------------|
| 0 - 3 | Weak           |
| 4     | Okay           |
| 5 - 6 | Good           |
| 7     | Strong         |

The application also checks if the password appears in `common.txt` — if so, it warns the user regardless of score.

---

## 🖥️ Getting Started

### Prerequisites

- Python 3.x installed (tested on Python 3.7+)  
- `tkinter` GUI library (usually comes pre-installed with Python)  
- `common.txt` — a plaintext file containing common passwords, one per line

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/PasswordStrengthChecker.git
   cd PasswordStrengthChecker

2. Prepare common.txt:

Make sure the common.txt file is present in the same directory as checker.py. You can use your own list or download a popular common passwords list from the internet (e.g., from SecLists).

3. Run the application:

   python checker.py

##File Structure 

PasswordStrengthChecker/
│
├── checker.py          # Main Python script with GUI and logic
├── common.txt          # List of common passwords (one per line)
├── README.md           # This README file
└── requirements.txt    # (Optional) Dependencies if any

##💡 Usage
Launch the app and enter your password in the input field.

The strength score and classification will update based on your input.

If your password matches a common password, you'll get a warning.

Use the feedback to create a stronger password.

##⚙️ Customization
Update common passwords: Edit common.txt to add or remove entries.

Adjust scoring: Modify the scoring rules inside checker.py to fit your own criteria.

UI changes: Customize fonts, colors, and layout in the tkinter code.

##🤝 Contributing
Contributions are welcome! Feel free to:

Report bugs

Suggest new features

Submit pull requests for improvements

Please follow standard git workflow and add clear commit messages.
