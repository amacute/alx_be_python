# explore_datetime.py

# Changed import statement to specifically import datetime and timedelta classes
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and prints the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    Returns the current datetime object.
    """
    # Use datetime.now() directly as it's imported
    current_date = datetime.now() 
    # Format and print the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date # Return the datetime object for use in other functions

def calculate_future_date(current_date):
    """
    Prompts the user to enter a number of days, calculates a future date
    by adding those days to the current_date, and prints it in "YYYY-MM-DD" format.

    Args:
        current_date (datetime.datetime): The base datetime object to add days to.
    """
    try:
        # Prompt user for a number of days
        days_to_add_str = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_to_add_str) # Convert input to an integer

        # Calculate the future date using timedelta
        # Use timedelta directly as it's imported
        future_date = current_date + timedelta(days=days_to_add)
        # Format and print the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

    except ValueError:
        # Handle cases where the user enters non-integer input for days
        print("Invalid number of days. Please enter a whole number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    # Store the returned current_date to pass to the next function
    current_dt = display_current_datetime()

    # Part 2: Calculate a future date
    calculate_future_date(current_dt)


