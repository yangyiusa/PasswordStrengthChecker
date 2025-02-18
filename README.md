# PasswordStrengthChecker

A simple Python script that evaluates the strength of a user-provided password based on length, character variety, and checks against a list of commonly used (and often breached) passwords. It outputs a score from 0 to 100 and provides feedback on how secure the password might be.

---

## What This Program Does

1. **Loads Common Passwords:** It optionally loads a list of known weak/common passwords from a text file (`common_passwords.txt`).  
2. **Calculates Strength Score (0-100):**  
   - Checks the length of the password (more points for longer passwords).  
   - Checks if it includes a mix of lowercase letters, uppercase letters, digits, and special characters.  
   - Penalizes if the password is on the known common/breached password list.  
3. **Provides Feedback:**  
   - Rates the password as *Weak*, *Moderate*, or *Strong*.  
   - Gives a short message about how to improve if necessary.  

---

## How to Run

1. **Clone or Download this Repository:**  
   Ensure you have `password_checker.py` (or the file containing the code) and `common_passwords.txt` (optional) in the same directory.

2. **Install Dependencies:**  
   - Python 3.7+ (Recommended)  
   - No external libraries are strictly required. The script uses only Python’s standard library (`re`, `os`).

3. **Prepare `common_passwords.txt` (Optional):**  
   - A list of common or compromised passwords, one per line.  
   - If the file is not present, the script will still run but will warn you that the file was not found, and checks for commonly known passwords will be skipped.

4. **Run the Script:**  
   ```bash
   python password_checker.py


Limitations
Educational Purpose Only:
This tool is meant to demonstrate basic password checking logic. It should not be used as a standalone security measure or relied upon for critical systems.

Not a Comprehensive Security Solution:
Password strength is more nuanced and can be influenced by multiple factors (e.g., brute force time, dictionary attacks, context-based vulnerabilities). This script does not account for all real-world attack vectors.

Potential False Sense of Security:
A high score here does not guarantee absolute security. Attackers can still exploit breaches, phishing, or other techniques to obtain passwords. Always follow best security practices.

Ethical Considerations & Responsible Use
Responsible Usage:

Use this script only on passwords you are authorized to test.
Do not store or share any passwords tested.
Do not modify this script to capture or misuse sensitive data.
Potential Misuse:

Someone could adapt this to log and store passwords entered, which would be malicious.
There is a risk that users may trust the output too heavily. Always educate users about broader security hygiene.
Reporting & Disclosure:

If you suspect security flaws in this script, please report them responsibly.
This project is intended to raise awareness on password hygiene, not to be a production-grade solution.
Contributing
Feel free to open issues or submit pull requests to improve functionality or fix bugs. Since this is an educational tool, we welcome enhancements that help demonstrate security best practices and highlight pitfalls of simplistic password checks.

License
MIT License
You are free to use, modify, and distribute this script as per the MIT license terms.