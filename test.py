#Choose a value that you would like to find the multiples of
div = int(input("Choose a denominator: "))
newList = []
x = 0

#Find the multiples of your chosen value from 0 to 1000 including 1000.
while x <= 1000:
    if x % div == 0:
        newList.append(x)
        x += 1
    else:
        x += 1

#Print a list of all the multiples found
print(newList)