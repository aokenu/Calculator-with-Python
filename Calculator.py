import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

"""Defining a dictionary for the different mathematical operations"""
math_dict = {"add" : "+", "divide" : "/", "subtract" : "-", "multiply" : "*" }

def calculate():
    # input for the first number (n1)
    n1 = int(input("What is the first number ?:"))
    for key in math_dict:
        print(math_dict[key])

    should_continues = True

    # This code defines the
    while should_continues:
        ops = input("Pick an operation :")
        if ops == "+":
            ops_choice = add
        elif ops == "/":
            ops_choice = divide
        elif ops == "-":
            ops_choice = subtract
        elif ops == "*":
            ops_choice = multiply
        else:
            print("You have not selected any operation, please select an operation to continue")

        n2 = int(input("What's the second number ?:"))

        output = ops_choice(n1, n2)
        print(f"{n1} {ops} {n2} = {output}")

        choice = input(print(f"Type 'y' to continue calculating with {output}, or 'n' to start a new calculation :"))
        if choice == 'y':
            n1 = output
        else:
            should_continues = False
            print("\n" * 50)
            calculate()

calculate()


