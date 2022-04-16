dicc = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

name = input("What is your name?\n")
sentence = input("Type a sentence:\n")

score = 0

for letter in sentence.upper():
    for key, value in dicc.items():
        if letter in value:
            score += key

def open_and_print_file(file):
    try:
        with open(file,"r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File not found")
        raise
    finally:
        print("\n execution complete")

def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise

write_to_file("orders.txt", f" Name: {name}\n Sentence: {sentence}\n Score: {score}\n")
open_and_print_file("orders.txt")
