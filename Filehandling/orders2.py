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

write_to_file("orders.txt","Testing")
open_and_print_file("orders.txt")