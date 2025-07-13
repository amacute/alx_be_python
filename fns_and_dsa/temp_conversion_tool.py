# temp_conversion_tool.py

# Define Global Conversion Factors
# These factors are accessible by functions throughout the script.
# Removed spaces around '/' to match strict checker requirements
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using a global conversion factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR for conversion
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using a global conversion factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR for conversion
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction for temperature conversion.
    It prompts for temperature and unit, then performs and displays the conversion.
    """
    try:
        # Prompt the user to enter a temperature
        temp_input = input("Enter the temperature to convert: ")
        # Convert input to float; raises ValueError if not numeric
        temperature = float(temp_input) 

        # Prompt for the unit (C/F) and convert to uppercase for consistent checking
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        # Raise the specified error message for non-numeric temperature input
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        # Catch any other unexpected errors during execution
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure the main function runs when the script is executed directly
    main()

        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

