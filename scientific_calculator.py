import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."
def power(x, y):
    return x ** y
def square_root(x):
    return math.sqrt(x)
def log(x, base=10):
    return math.log(x, base)
def sine(x):
    return math.sin(math.radians(x))
def cosine(x):
    return math.cos(math.radians(x))
def tangent(x):
    return math.tan(math.radians(x))
def factorial(x):
    if x < 0:
        return "Error: Factorial is not defined for negative numbers."
    else:
        return math.factorial(x)
def main():
    print("Scientific Calculator")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")
    print("12. Exit")
    while True:
        choice = input("\nEnter your choice (1-12): ")
        if choice == '12':
            print("Exiting calculator. Goodbye!")
            break
        elif choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
                elif choice == '5':
                    print("Result:", power(num1, num2))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        elif choice == '6':
            try:
                num = float(input("Enter number: "))
                print("Result:", square_root(num))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '7':
            try:
                num = float(input("Enter number: "))
                base = float(input("Enter base (default is 10): ") or 10)
                print("Result:", log(num, base))
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif choice == '8':
            try:
                num = float(input("Enter angle in degrees: "))
                print("Result:", sine(num))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '9':
            try:
                num = float(input("Enter angle in degrees: "))
                print("Result:", cosine(num))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '10':
            try:
                num = float(input("Enter angle in degrees: "))
                print("Result:", tangent(num))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '11':
            try:
                num = int(input("Enter an integer: "))
                print("Result:", factorial(num))
            except ValueError:
                print("Invalid input! Please enter an integer.")
        else:
            print("Invalid choice! Please enter a number from 1 to 12.")
if __name__ == "__main__":
    main()