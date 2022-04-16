list1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
list2 = ['D', 'G']
list3 = ['B', 'C', 'M', 'P']
list4 = ['F', 'H', 'V', 'W', 'Y']
list5 = ['K']
list6 = ['J', 'X']
list7 = ['Q', 'Z']

string = "Object oriented programming is a programming paradigm that uses objects and classes in programming"
score = 0

for letter in string.upper():
    if letter in list1:
        score += 1
    elif letter in list2:
        score += 2
    elif letter in list3:
        score += 3
    elif letter in list4:
        score += 4
    elif letter in list5:
        score += 5
    elif letter in list6:
        score += 8
    elif letter in list7:
        score += 10

print(f"The score for the sentence that you passed is: {score}")
