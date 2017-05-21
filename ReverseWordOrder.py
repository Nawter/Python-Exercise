# Write a function that asks the user for a string containing multiple words. Print back
# to the user the same string, except with the words in backwards order.
def reverseV1(w):
    return ' '.join(w.split()[::-1])

def reverseV2(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0,word)
    return " ".join(result)

def reverseV3(x):
    y = x.split()
    return " ".join(reversed(y))

def reverseV4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)


# test code
test = input("Enter a sentence: ")
print(reverseV1(test))
print(reverseV2(test))
print(reverseV3(test))
print(reverseV4(test))
