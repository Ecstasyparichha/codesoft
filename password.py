import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    
    if length <= 0:
        print("Please enter a valid length.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
