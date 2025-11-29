try:
    num1=int(input("Enter the numerator :"))
    num2=int(input("Enter the denominator :"))
    result=num1/num2
    print(f"The result is : {result}")
except ZeroDivisionError:
    print("Error : You cannot divide by zero!")
except ValueError:
    print("Error : Please enter a valid integer!") 