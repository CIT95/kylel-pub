# Calculator
# from art import logo
from os import system, name

# Clear old calculations

# Not sure if there
# are supposed to be separate clears
# but it still works.


def clear():
    if name == 'nt':
        a_ = system('cls')
    else:
        b_ = system('clear')


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Division
def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    # print(logo)

    num1 = float(input("What's the first number?:"))
    # Operations was misspelled.
    for symbol in operations:
        print(symbol)
    should_cont = True

    while should_cont:
        operation_symbol = input("Pick an operation from above: ")
        # Did not have a closing parentheses
        num2 = float(input("What's the second number?:"))
        calculation_funct = operations[operation_symbol]
        answer = calculation_funct(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f'Type "y" to continue calculating with {answer}  or '
                 'Type "n" to start a new calculation: ') == "y":
            num1 = answer
        else:
            should_cont = False
            # Calculator was running before clear.
            clear()
            calculator()

# Calculator was misspelled.


calculator()
