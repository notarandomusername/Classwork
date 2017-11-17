#basic strings
a = "hi"
b = "hello"

print(a, b)
print("greetings")

#using f for strings
import random

a = random.randint(1,10)
print(f"{a}")

#brackets
x = "Life"
y = "fun!"

print("{} is {}".format(x, y))
print("{1} is {0}".format(x, y))

f_string = "{} {}"

print(f_string.format("hello", "friend"))

math_string = "{} + {} = {}"

print(math_string.format(2, 2, 4))

#join
a = "Hello"
b = "friend!"

print(" ".join((a, b)))

#new line
print("new\nline")

#long string
long_string = """h
e
l
l
o
"""

print(long_string)