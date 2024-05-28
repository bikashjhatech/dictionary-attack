**Dictionary Attack Implementation**
This Python script implements a dictionary attack, a type of brute-force attack used to crack passwords by systematically checking each word in a predefined list of words (the "dictionary") against a hashed password.


**Requirements**
* Python 3.11.6
* passwordList.txt: A file containing a list of passwords to be checked against the hashed password.


**How to Run**
1. Make sure you have Python installed on your system.
2. Place the passwordList.txt file in the same directory as the script.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script by executing the following command:  python password_cracker.py
6. The script will check each password in the passwordList.txt file against the hashed password provided in the passwordCrack function.

**Implementation Details**
* The script reads passwords from the passwordList.txt file and hashes each password using the MD5 hashing algorithm.
* It then compares the hashed password with the input password hash.
* If a match is found, it prints the password that matches the hash.
* If no match is found, it prints a message indicating that the password was not found in the list.

