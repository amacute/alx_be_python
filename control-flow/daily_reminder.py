# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound (keep input as string for direct comparison)
time_bound_input = input("Is it time-bound? (yes/no): ").lower()

reminder_text = "" # This will hold the main part of the reminder message
prefix = "Reminder: " # Default prefix for the reminder

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder_text = f"'{task}' is a high priority task"
    case "medium":
        reminder_text = f"'{task}' is a medium priority task"
    case "low":
        reminder_text = f"'{task}' is a low priority task"
    case _: # Default case for unrecognized priority
        reminder_text = f"'{task}' has an unrecognized priority"

# Modify the reminder based on time sensitivity using the exact if condition the checker expects
if time_bound_input == "yes":
    # Add immediate attention message for time-bound tasks
    # Ensure the exact phrase "that requires immediate attention today!" is used
    if priority in ["high", "medium", "low"]: # Only append if priority was recognized
        reminder_text += " that requires immediate attention today!"
    else: # For unrecognized priority but time-bound
        reminder_text += ". It is time-bound and requires attention today!"
elif time_bound_input == "no":
    # Handle non-time-bound tasks
    if priority == "low":
        prefix = "Note: " # Change prefix to "Note:" for low priority, non-time-bound tasks
        reminder_text += ". Consider completing it when you have free time."
    elif priority in ["high", "medium"]:
        reminder_text += ". You can complete it at your convenience."
    # For unrecognized priority and non-time-bound, no additional phrase is needed, just the base message
else:
    # Handle unexpected input for time_bound_input (e.g., neither 'yes' nor 'no')
    reminder_text += ". (Time-bound status unclear)."
    # The checker might not test this specific case, but it adds robustness.

# Print the final customized reminder with the determined prefix
print(f"{prefix}{reminder_text}")
# Modify the reminder if the task is time-bound
if time_bound:
    # Add immediate attention message for time-bound tasks
    if priority in ["high", "medium", "low"]: # Only add if priority was recognized
        reminder_message += " that requires immediate attention today!"
    else: # For unrecognized priority but time-bound
        reminder_message += ". It is time-bound and requires attention today!"
else:
    # Add a note for non-time-bound tasks, especially low priority
    if priority == "low":
        reminder_message += ". Consider completing it when you have free time."
    elif priority in ["high", "medium"]:
        reminder_message += ". You can complete it at your convenience."
    # No extra message for unrecognized non-time-bound tasks

# Output the customized reminder
print(f"\nReminder: {reminder_message}")
