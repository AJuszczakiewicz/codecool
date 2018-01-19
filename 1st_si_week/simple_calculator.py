import operator

ops = { 
    "+": operator.add, 
    "-": operator.sub, 
    "*": operator.mul,  
    "/": operator.truediv, 
    "**": operator.pow, 
    "%": operator.mod 
    }

num1 = input("Enter a number (or a letter to exit): ")
while num1.isdigit():
    op = input("Enter an operation: ")
    num2 = input("Enter another number: ")
    print("Result: " + str(ops[op](float(num1), float(num2))))
    num1 = input("Enter a number (or a letter to exit): ")

