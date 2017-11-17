# While loop 1
# Make a list of numbers less than 10
newList = []
x = 0

while x < 10:
    newList.append(x)
    x += 1

print(newList, "\n")

# While loop 2
# Add all numbers less than 30 to each other
x = 0
y = 0

while x < 30:
    y += x
    x += 1

print(y, "\n")

# While loop 3
# Generate two random lists, and print the shared numbers.
import random

listOne = []
listTwo = []
listThree = []
x = 0

while x <= 100:
    listOne.append(random.randint(1,100))
    listTwo.append(random.randint(1,100))
    x += 1

for item in listOne:
    if item in listTwo:
        listThree.append(item)
        x += 1

print(listThree, "\n")

# While loop 4
# Print multiples of both 5 and 7 from 1 to 1000
x = 1
listA = []

while x <= 1000:
    if x % 5 == 0 and x % 7 == 0:
        listA.append(x)
        x += 1
    else:
        x += 1

print(listA, "\n")

# While loop 5
# Print the multiples of 3 from 1 to a number chosen by the user

x = 1
y = int(input("Choose a number: "))
listA = []

while x <= y:
    if x % 3 == 0:
        listA.append(x)
        x += 1
    else:
        x += 1

print(listA)