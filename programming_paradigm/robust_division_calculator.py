# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division, robustly handling ZeroDivisionError and ValueError.

    Args:
        numerator: The numerator for the division.
        denominator: The denominator for the division.

    Returns:
        str: An error message if division is not possible, or the float result.
    """
    try:
        # Attempt to convert arguments to floats
        num = float(numerator)
        den = float(denominator)

        # Handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        # Catch non-numeric input errors
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"
