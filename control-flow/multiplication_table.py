# multiplication_table.py

try:
    # Prompt user for a number
    number_str = input("Enter a number to see its multiplication table: ")
    number = int(number_str) # Convert input to an integer

    print(f"\nMultiplication table for {number}:")
    # Generate and print the multiplication table using a for loop
    for i in range(1, 11): # Loop from 1 to 10 (inclusive)
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    # Handle cases where input is not a valid integer
    print("Invalid input. Please enter a whole number.")
except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
