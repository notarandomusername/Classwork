#Initialize x to the value of one as we want to start from 1.
x = 1
#Define a blank list which will later hold all values.
listA = []

#Set up a while loop to print all values from 1 to 10000.
while x <= 10000:
    #If x is divisible by both 3 and 11, print motorcycle in its place.
    if x % 3 == 0 and x % 11 == 0:
        listA.append("motorcycle")
        x += 1
    #If x is divisible by only 3, print bicycle in its place.
    elif x % 3 == 0:
        listA.append("bicycle")
        x += 1
    #If x is divisible by only 11, print car in its place.
    elif x % 11 == 0:
        listA.append("car")
        x += 1
    #If none of those conditions are met, print x.
    else:
        listA.append(x)
        x += 1

#Print the list.
print(listA)