# Divisors.py using python3
num = int(input("Please choose a number to divide: "))
listRange = list(range(1,num+1))
print(range(1,num+1))
divisorList = []
for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
