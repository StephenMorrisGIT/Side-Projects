import random
import string
# Get user input for the number of characters to use
length = int(input("Enter Password Length: "))
def generate_password(length):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Generate a password of length 12
password = generate_password(length)
print(password)

confirmation = input("Confirm Password (y/n): ")
for i in range(3):
    if confirmation == 'y' or confirmation == 'n':
        if confirmation == 'y':
            print("Password Confirmed")
            break
        else:
            print("Password not confirmed")
            break
    else:
        confirmation = input("Confirm Password (y/n): ")
        continue


