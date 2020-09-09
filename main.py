def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divades(a, b):
    return a / b

def power(a, b):
    return a ** b

#funkcja formatująca, nie wykonuje żadnych obliczeń
def print_calculation(a, b, sign, result):
    print (f"Your math operation is: {a} {sign} {b} = {result}" )

def main():
    print("enter first number: ")
    a = float(input())

    print("enter second number: ")
    b = float(input())

    print("Give a math operation: ")
    sign = input()

    result = 0

    if sign == "+":
        result = add(a, b)
    elif sign == "-":
        result = substract(a, b)
    elif sign == "*":
        result = multiplication(a, b)
    elif sign == "/":
        result = divades(a, b)
    elif sign == "**":
        result = power(a, b)

    print_calculation(a, b, sign, result)

    print ("Good Bye")

main()