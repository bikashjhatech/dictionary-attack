
import hashlib

def passwordCrack(inputPassword):
    try:
        with open("passwordList.txt", "r") as passwordFile:
            for password in passwordFile:
                encodedPassword = password.strip().encode("utf-8")
                digest = hashlib.md5(encodedPassword).hexdigest()
                if digest == inputPassword:
                    print("Password has been found: " + password)
                    return  
        print("Password not found in the list.")

    except FileNotFoundError:
        print("There is no file named as passwordList.txt")

if __name__ == '__main__':
    passwordCrack("5f4dcc3b5aa765d61d8327deb882cf99")

    



