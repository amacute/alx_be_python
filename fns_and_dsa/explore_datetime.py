# explore_datetime.py

import datetime

def display_current_datetime():
    """
    Displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date # Return current_date for potential use in other functions

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates a future date.

    Args:
        current_date (datetime.datetime): The base date from which to calculate.
    """
    try:
        days_to_add_str = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_to_add_str)

        # Calculate the future date
        future_date = current_date + datetime.timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

    except ValueError:
        print("Invalid input. Please enter a whole number for days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Part 1: Display current date and time
    current_dt = display_current_datetime()

    # Part 2: Calculate a future date
    calculate_future_date(current_dt)
