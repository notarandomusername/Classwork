from random import randrange
listA = [randrange(1,100) for x in range (100)]
listB = [randrange(1,100) for x in range (100)]
listC = []

for item in listA:
    if item in listB:
        listC.append(item)

print(listC)