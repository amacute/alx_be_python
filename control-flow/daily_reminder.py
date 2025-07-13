# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
time_bound_str = input("Is it time-bound? (yes/no): ").lower()
time_bound = time_bound_str == "yes" # Convert to boolean

reminder_message = "" # Initialize reminder message

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _: # Default case for invalid priority
        reminder_message = f"'{task}' has an unrecognized priority"

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
