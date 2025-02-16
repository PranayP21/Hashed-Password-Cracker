import hashlib

# 'hashlib' is a built-in Python Library used for hashing strings with algoritms
# Hashing is a one-way function, making it useful for storing passwords securely

# Hashing function (MD5, SHA-256, etc.)
def hash_password(password, algorithm="md5"):
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm.")
    
    # What does the above function do
    # 1. Takes plaintext password and hashes it using a specified algorithm 
    # 2. Default hashing algorithm is 'md5' however 'sha256' is also supported 
    # 3. Coverts the password into a hash digest

    # How it works
    # 1. password.encode coverts the string to bytes
    # 2. hashlib.md5(...).hexdigest() coverts it into a hexadecimal hash 
    # 3. If the algorithm is not supported, it raises an error

# Function to crack the hash using a dictionary attack
def crack_password(hash_to_crack, wordlist, algorithm="md5"):
    with open(wordlist, "r", encoding="utf-8") as file:
        for word in file:
            word = word.strip()
            hashed_word = hash_password(word, algorithm)
            if hashed_word == hash_to_crack:
                return f"Password found: {word}"
    return "Password not found."

    # What Does This Function Do
    # 1. Opens a wordlist file (e.g., common_passwords.txt).
    # 2. Reads passwords line by line, removing extra spaces (.strip()).
    # 3. Hashes each password using the hash_password function.
    # 4. Compares the hashed word with hash_to_crack.
    # 5. If a match is found, it returns "Password found: {word}".
    # 6. If no match is found, it returns "Password not found.".

    # How It Works?
    # 1. This function performs a dictionary attack, checking if the hashed version of any word in the list matches the target hash.

# Example usage
if __name__ == "__main__":
    # Replace with actual hashed password
    target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # Hashed version of "password"
    wordlist_file = "common_passwords.txt"  # A file containing common passwords

    result = crack_password(target_hash, wordlist_file)
    print(result)

    # What Does This Do?
    # 1. Checks if the script is run directly (__name__ == "__main__").
    # 2. Sets a target hash (MD5 of "password").
    # 3. Uses crack_password to find the original password.
    # 4. Prints the result.
