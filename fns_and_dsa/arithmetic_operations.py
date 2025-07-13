# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the given numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message for division by zero.
    """
    op = operation.lower()
    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 == 0:
            # Handle division by zero
            return "Cannot divide by zero!"
        else:
            return num1 / num2
    else:
        # Handle invalid operation input
        return "Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
