import math


def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        else:
            return num1 / num2
    elif operator == "sqrt":
        if num1 < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        else:
            return math.sqrt(num1)
    elif operator == "**":
        return num1**num2
    else:
        raise ValueError("Invalid operator")


def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /, sqrt, **): ")
            result = calculator(num1, num2, operator)
            if operator == "sqrt":
                print(f"{operator}({num1}) = {result}")
            else:
                print(f"{num1} {operator} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting calculator...")
            break


if __name__ == "__main__":
    main()
