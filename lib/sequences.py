#!/usr/bin/env python3

def print_fibonacci(length):
    fib = [0, 1]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])
    print(fib[:length])


    pass

# my_list = [('Ann', 2), ('Bianca', 1), ('Jenny', 3)]

# def sort_tuple(tuple_value):
#     return tuple_value[0]
# my_list.sort(key = sort_tuple)
# print(my_list)

# for n in range(0, 10, 2):
#     print(n)

#     my_string = ["zina", "ifeoma", "neya", "orji"]
#     new_string = []
    
#     for string in my_string:
#         new_string.append(string.title())
#     print(new_string)

# my_string = "rest in peace mommy"
# new_string = my_string.title()
# print(new_string)
