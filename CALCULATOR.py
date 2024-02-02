#*** DESIGN A SIMPLE CALCULATOR USING ARITHMETIC OPERATIONS ***#
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def calculator():
    print("\nSimple Calculator\n")
    while True:
        try:
            # Get user input2

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operation (+, -, *, /): ")

            # Perform calculation based on the operator
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                result = "Invalid operator"

            # Display the result
            print(f"\nResult: {result}\n")

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
calculator()
