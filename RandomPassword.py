# Generate a random password using internal functions from python.
import string
import random

def passwordGenerator(size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for x in range(size))

print(passwordGenerator(int(input('How many characters in your password:'))))
