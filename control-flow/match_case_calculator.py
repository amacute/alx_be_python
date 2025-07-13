# match_case_calculator.py

try:
    # Prompt for user input for two numbers
    num1_str = input("Enter the first number: ")
    num1 = float(num1_str) # Convert to float to handle decimal numbers

    num2_str = input("Enter the second number: ")
    num2 = float(num2_str) # Convert to float

    # Ask for the type of operation
    operation = input("Choose the operation (+, -, *, /): ")

    result = None # Initialize result variable

    # Perform the calculation using Match Case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            # Handle division by zero case
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _: # Default case for invalid operation
            print("Invalid operation. Please choose from +, -, *, /.")

except ValueError:
    # Handle cases where input numbers are not valid
    print("Invalid number input. Please enter valid numerical values.")
except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
