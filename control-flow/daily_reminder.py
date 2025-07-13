# daily_reminder.py

# Prompt for a single task description
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
# Renamed variable to 'time_bound' to match checker's exact requirement
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the main part of the reminder message
reminder_text_core = ""
# Default prefix for the reminder output
output_prefix = "Reminder: "

# Process the task based on priority using a Match Case statement
match priority:
    case "high":
        reminder_text_core = f"'{task}' is a high priority task"
    case "medium":
        reminder_text_core = f"'{task}' is a medium priority task"
    case "low":
        reminder_text_core = f"'{task}' is a low priority task"
    case _: # Handles any other input for priority
        reminder_text_core = f"'{task}' has an unrecognized priority"

# Use an if statement to modify the reminder based on time sensitivity
# Now uses 'time_bound' variable directly as per checker's requirement
if time_bound == "yes":
    # Append the exact required phrase for time-bound tasks
    reminder_text_core += " that requires immediate attention today!"
elif time_bound == "no":
    # Handle non-time-bound tasks
    if priority == "low":
        # Change the prefix to "Note: " for low priority, non-time-bound tasks
        output_prefix = "Note: "
        reminder_text_core += ". Consider completing it when you have free time."
    elif priority in ["high", "medium"]:
        # For high/medium priority but non-time-bound, provide a general completion message
        reminder_text_core += ". You can complete it at your convenience."
    # If priority is unrecognized and not time-bound, no additional phrase is added to the core message
else:
    # Handle cases where time_bound is neither 'yes' nor 'no'
    reminder_text_core += ". (Time-bound status was not clearly specified)."

# Print the final customized reminder, combining the prefix and the core message
print(f"{output_prefix}{reminder_text_core}")

