# Hashed-Password-Cracker
This project provides a simple password hash cracker using a dictionary attack in Python. It includes a function to hash passwords using MD5 or SHA-256 and a function to compare a given hash against a wordlist of common passwords. The script reads passwords from a file, hashes them, and checks if they match the target hash. If a match is found, the original password is revealed. This tool is intended for educational and ethical cybersecurity purposes only. Unauthorized use for cracking passwords without permission is illegal.

For better results, larger password lists like rockyou.txt can be used to increase the chances of finding a match. RockYou.txt contains millions of real-world passwords and is commonly used in penetration testing.

🔹 Potential Enhancements
✅ Multi-threading: Speed up cracking by using parallel processing.
✅ Brute Force Mode: Generate passwords instead of using a wordlist.
✅ Support More Algorithms: Add bcrypt, SHA-512, etc.
✅ Salting: Handle hashes with salts for security.
