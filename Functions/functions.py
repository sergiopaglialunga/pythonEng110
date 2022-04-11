def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1,2,3,4,5,6,7,8,"John")

