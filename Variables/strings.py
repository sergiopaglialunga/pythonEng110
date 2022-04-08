# # escape caracter
# # quotes = 'Eng said \n\t"He\'s good"'
# # \n new line
# # \t new tab
# # print(quotes)
# s = "Hello World"
# # c = s[6] # indexing
# # print(c)
# #
# # # string slicing
# # slice = s[6:9] # inclusive of 6 exclusive of 9
# # slice = s[:8]
# # slice = s[8:]
# # slice = s[1:10:2]
# # slice = s[::-1]
# #
# # # methods
# # s= "Engineering 110"
# #
# # print(s.lower())
# # print(s.upper())
# # print(s.capitalize())
# # print(s.strip())
# # print(s.replace('e', 'ooo').upper().replace('E','000'))
#
# # print(slice)
#
#
# number = 10
# fruit = "apples"
#
# print(f"There are {str(number)} {fruit}")
#
# name = input("What is your name?:\n")
# age: str = input("How old are you?:\n")
#
# print(f"Your name is {name}, and your are {age} years old")
# print(type(age))
# # Use inputs to ask a few questions of the user
# # Try to collect text and numbers
# # Respond with a message that includes the input entries
#
# # boolean
# a = 10
# print(a >= 2 and a % 2 == 0) # a is even
#
hi = "Hello World"
print(hi.startswith("Hell"))
a = "alpha"
print(a.isalpha())
l = "lowercase"
print(l.islower())
#
# print(hi.isalpha())

trial = 0
print(f"{trial} is treated as {bool(trial)}")

x = None
print(x, type(x))

print(bool(None))
print(x is False)
print(x is None)