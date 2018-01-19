import sys

params_dict = {
    "v" : "version 0.02",
    "a" : "author: Alex, sponsored by Codecool",
    "h" : "help not found"
}

def has_params(params):
    if params[1:]: 
        return True
    else: 
        return False

def names(params_list):
    names = []
    for x in params_list[1:]:
        if x[0] != "-":
            names.append(x)
    return names

def options(params_list):
    options = []
    for x in params_list[1:]:
        if x[0] == "-":
            for y in x[1:]:
                options.append(y)
    return options

def print_names(names):
    if names:
        for x in names:
            print("Hello {}!".format(x))

def print_options(options):
    if options:
        for x in options:
            print(params_dict[x])

def print_hello(params_list):
    if has_params(params_list):
        print_options(options(params_list))
        print_names(names(params_list))
    else:
        print("Hello World")


print_hello(sys.argv)