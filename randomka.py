import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        user_length = int(input("Password length: "))
        password = generate_password(user_length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Error: Enter a number!")