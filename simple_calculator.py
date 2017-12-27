import operator

num1 = input("Enter a number (or a letter to exit): ")
while num1.isdigit():
    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "**": operator.pow, "%": operator.mod }
    op = input("Enter an operation: ")
    num2 = input("Enter another number: ")
    print("Result: " + str(ops[op](float(num1), float(num2))))
    num1 = input("Enter a number (or a letter to exit): ")
