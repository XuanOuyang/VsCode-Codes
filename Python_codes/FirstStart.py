def adding (num: int, dig: int):
    sum = num + dig
    print(sum)

def sometests(x: int):
    y = int
    z = x * y / 2
    print(z)

def quickCalc(number1: int, operator: str, number2: int):
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    elif operator == "//": # this rounds it to the nearest whole number
        result = number1 // number2
    elif operator == "**": # ** can act as both exponent and log, if it is -4 ** 2 the operation applies before the - so the answer would be 16 | you can also you this for square roots since 2^0.5 = sqaure root
        result = number1 ** number2
    else:
        print("Invalid operator")
        return
    
    print(f"The result of {number1} {operator} {number2} is {result}")

# Get user input for the numbers and operator
user_input1 = int(input("Please enter the first number: "))
user_operator = input("Please enter the operator (+, -, *, /, //, **): ")
user_input2 = int(input("Please enter the second number: "))

# Call the quickCalc functions
quickCalc(user_input1, user_operator, user_input2)