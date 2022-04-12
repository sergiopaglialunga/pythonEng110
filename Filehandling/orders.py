def open_and_print_file(file):
    try:
        opened_file = open(file,"r")
        file_line_list = opened_file.readlines()

        print(file_line_list)

        for line in file_line_list:
            print(line.rstrip('\n'))

        opened_file.close()

    except FileNotFoundError:
        print("File not found")
        raise

open_and_print_file("orders.txt")