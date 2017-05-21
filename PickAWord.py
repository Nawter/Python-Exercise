import random

words = []
with open('sowpods.txt','r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)


randomIndex = random.randint(0, len(words))

print("Random word:" , words[randomIndex])
