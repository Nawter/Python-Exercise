# Check prime numbers using functions
def get_number(str):
    '''Returns integer value for input. Prompt is displayed text'''
    return int(input(str))

def is_prime(number):
    #Basic cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes
    else:
        prime = True
        for checkNumber in range (2, (number // 2) + 1):
            if number % checkNumber == 0:
                prime = False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not "
    print(number, " is ", descriptor, "prime.", sep = "", end = "\n\n")
# never ending loop
while 1 == 1:
    print_prime(get_number("Enter a number to check. Ctrl-C to exit:"))
