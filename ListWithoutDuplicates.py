# write a function that takes a list and return a new list without duplicates.
# Without sets
def deleteDuplicates(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y
# This solution using sets
def deleteDuplicatesV2(x):
    return list(set(x))


a = [1,2,3,4,5,6,7,1,1,2,2,3,4]
print(a)
print(deleteDuplicatesV2(a))
print(deleteDuplicates(a))
