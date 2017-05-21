# List that contains first element and last element of the list.
aList = [5, 10, 15, 20, 25, 30]
def listEnds(aList):
    return [aList[0], aList[len(aList)-1]]

print(listEnds(aList))
