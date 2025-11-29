class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self._save_history(a, b, '+', result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history(a, b, '-', result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history(a, b, '*', result)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        result = a / b
        self._save_history(a, b, '/', result)
        return result

    def modulus(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        result = a % b
        self._save_history(a, b, '%', result)
        return result

    def _save_history(self, a, b, operator, result):
        self.history.append(f"{a} {operator} {b} = {result}")

    def show_history(self):
        if not self.history:
            return "No calculations performed yet."
        return "\n".join(self.history)


# Main program
calc = Calculator()

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Show History")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice == '7':
        print("Exiting the calculator.")
        break
    elif choice == '6':
        print("\nCalculation History:")
        print(calc.show_history())
    elif choice in {'1', '2', '3', '4', '5'}:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print("Result:", calc.add(num1, num2))
        elif choice == '2':
            print("Result:", calc.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calc.multiply(num1, num2))
        elif choice == '4':
            print("Result:", calc.divide(num1, num2))
        elif choice == '5':
            print("Result:", calc.modulus(num1, num2))
    else:
        print("Invalid choice. Please select a valid option.")
