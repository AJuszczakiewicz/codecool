import sys

def has_params(params):
    if params[1:]: return True
    else: return False

def options(params_list):
    options = []
    for x in params_list[1:]:
        if x[0] == "-":
            for y in x[1:]:
                options.append(y)
    return options

def print_options(options, num_list):
    if options:
        for x in options:
            print(params_dict[x](num_list))

def get_input():
    num_list = input("Gimme some numbers to sort: ").split(", ")
    print(num_list)
    return num_list

def bubble(num_list):
    for j in range(0, len(num_list)-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list

def codecool_sort(num_list):
    for x in range(0, len(num_list)-1):
        bubble(num_list)
    return num_list

def quick_sort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1], x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quick_sort(x[:i])
        second_part = quick_sort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def merge_sort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
        return merge(a,b)

def print_sort(num_list, params):
    if has_params(params):
        print_options(options(params), num_list)
    else: print(codecool_sort(num_list))

params_dict = {
    "q" : quick_sort,
    "m" : merge_sort,
    "b" : codecool_sort
}

print_sort(get_input(), sys.argv)

def test_codecool_sort():
    assert codecool_sort([3, 2, 6, 1, 67, 3, 5, 1]) == [1, 1, 2, 3, 3, 5, 6, 67]
    assert codecool_sort([2, 1]) == [1, 2]
    assert codecool_sort([]) == []

def test_merge_sort():
    assert merge_sort([3, 2, 6, 1, 67, 3, 5, 1]) == [1, 1, 2, 3, 3, 5, 6, 67]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([]) == []

def test_quick_sort():
    assert quick_sort([3, 2, 6, 1, 67, 3, 5, 1]) == [1, 1, 2, 3, 3, 5, 6, 67]
    assert quick_sort([2, 1]) == [1, 2]
    assert quick_sort([]) == []

# print(codecool_sort(get_input()))