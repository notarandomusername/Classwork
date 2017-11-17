#Import randint from random.
from random import randint
import sys

#Define some variables.
num1 = int(randint(1,10))
num2 = int(randint(1,10))
num3 = int(randint(1,10))

#Make conditional statements to check if something broke.
if num1 > 10 or num1 < 1:
    print("Number machine broke.")
    sys.exit()
elif num2 > 10 or num2 < 1:
    print("Number machine broke.")
    sys.exit()
elif num3 > 10 or num3 < 1:
    print("Number machine broke.")
    sys.exit()
else:
    print("""Working as intended.
    """)

#Print rules.
print("""Three numbers between one and ten will randomly generate.
Place a bet to try your luck!
If a number is greater than or equal to 9, your bet doubles!
If a number is less than or equal to 2, your bet halves!
If a number is seven, your bet doubles!
If two numbers match, you get your money back!
If all three match, you double your money!
If you get all sevens, you quadruple your money!
Good luck!
""")

#Define your bet variables.
bet = int(input("How much do you want to bet? "))
bal = bet

#Print out the numbers you got.
print("You got:", num1, num2, num3)

#Make conditional statements to print certain strings based on the presence of the number 7.
if num1 == 7 and num2 == 7 and num3 == 7:
    print("Jackpot! Your balance is:", bet*5 - bal)
    sys.exit()
elif num1 == 7 or num2 == 7 or num3 == 7:
    print("Lucky number 7! Your bet is now", bet*2, "so good luck!")
elif num1 >= 9 or num2 >= 9 or num3 >= 9:
    print("Big number, big prizes! Your bet is now", bet*2, "so good luck!")
elif num1 <= 2 or num2 <= 2 or num3 <= 2:
    print("Small number, small prizes. Your bet is now", bet*.5,"but still, good luck!")

#Make conditional statements to print certain strings based on certain values matching.
if num1 == num2 == num3:
    print("Big win! All numbers are the same! Your balance is:", bet*3 - bal)
elif num1 == num2:
    print("It's a match! Your first number and your second are the same! Your profit is:", bet*2 - bal)
elif num2 == num3:
    print("It's a match! Your second number and your third are the same! Your profit is:", bet*2 - bal)
elif num1 == num3:
    print("It's a match! Your first number and your third are the same! Your profit is:", bet*2 - bal)
else:
    print("No match! Better luck next time! Your profit is 0.")

sys.exit()