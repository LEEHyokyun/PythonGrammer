def sum_second(a, b):

    print_first(a, b)
    return a + b

def print_first(a, b):
    print(a, b)


def sum_first (a, b):
    print_second(a, b)
    return a + b

def print_second(a, b):
    print(a, b)



print(sum_second(1,2))
print(sum_first(3,4))

