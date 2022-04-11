# x = 0
#
# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1

user_prompt = True

while user_prompt:
    age = input("What is your age?\n")
    if age.isdigit() and int(age) <= 117:
        user_prompt = False
    elif not age.isdigit():
        print("You must enter a number")
    elif int(age) > 117:
        print("The number is out of range")

print(f"Your age is {age}")


