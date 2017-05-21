# Check prime numbers using list comprehension
num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
    if num > 1:
        if len(a) == 0:
            print ('Is prime number')
        else:
            print ('Not prime')
    else:
            print ('Not prime')
is_prime(num)
