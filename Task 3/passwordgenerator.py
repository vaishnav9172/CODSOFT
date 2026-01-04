import random
import string

# User input
length = int(input("Enter password length: "))

print("Choose password complexity:")
print("1. Low (Letters only)")
print("2. Medium (Letters + Numbers)")
print("3. High (Letters + Numbers + Special Characters)")

choice = int(input("Enter your choice (1/2/3): "))

# Define character sets
if choice == 1:
    characters = string.ascii_letters
    mandatory = [random.choice(string.ascii_letters)]

elif choice == 2:
    characters = string.ascii_letters + string.digits
    mandatory = [
        random.choice(string.ascii_letters),
        random.choice(string.digits)
    ]

elif choice == 3:
    characters = string.ascii_letters + string.digits + string.punctuation
    mandatory = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

else:
    print("Invalid choice")
    exit()

# Check length
if length < len(mandatory):
    print("Password length too short for selected complexity")
    exit()

# Generate remaining characters
password = mandatory
for i in range(length - len(mandatory)):
    password.append(random.choice(characters))

# Shuffle for security
random.shuffle(password)

# Display password
print("Generated Password:", "".join(password))
