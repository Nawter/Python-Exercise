# Find an element in a list using binary search.
def find(orderedList, elementToFind):
    startIndex = 0
    endIndex = len(orderedList) - 1
    found = False

    while startIndex <= endIndex and not found:
        middleIndex = (startIndex + endIndex) // 2
        if orderedList[middleIndex] == elementToFind:
            found = True
        else:
            if elementToFind < orderedList[middleIndex]:
                endIndex = middleIndex - 1
            else:
                startIndex = middleIndex + 1

    return found

if __name__=="__main__":
    l = [2, 4, 6, 8, 10]
    print(find(l, 5))
    print(find(l, 10))
    print(find(l, -1))
    print(find(l, 2))
