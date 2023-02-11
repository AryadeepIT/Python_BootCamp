def add(*args):  # can change *args to any word (ex - *arya)
    print(args[0])  # can be accessible by their index
    # print(args)   # type 'tuple'
    num = 0
    for n in args:   # have to change if change name above
        num += n    # doing sum of provided input
    return num


print(add(3, 5, 6))   # unlimited positional arguments
