# daily_reminder.py

# Prompt user for task details
task = input("Enter your task for today: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process the task using match-case based on priority
match priority:
    case "high":
        reminder = f"Your task: '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task: '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task: '{task}' is LOW priority."
    case _:
        reminder = f"Your task: '{task}' has an UNKNOWN priority."

# Modify reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)