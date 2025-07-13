# pattern_drawing.py

try:
    # Prompt user for pattern size
    size_str = input("Enter the size of the pattern (a positive integer): ")
    size = int(size_str) # Convert input to an integer

    if size <= 0:
        print("Pattern size must be a positive integer.")
    else:
        current_row = 0 # Initialize row counter for the while loop

        # Outer while loop: iterates through each row
        while current_row < size:
            # Inner for loop: prints asterisks for the current row
            for _ in range(size): # Loop 'size' times for columns
                print("*", end="") # Print asterisk without newline
            print() # Print a newline character after each row
            current_row += 1 # Increment row counter

except ValueError:
    # Handle cases where input is not a valid integer
    print("Invalid input. Please enter a whole number.")
except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")