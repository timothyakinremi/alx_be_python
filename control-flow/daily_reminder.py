# daily_reminder.py

# Prompt user for task details
Task = input("Enter your task for today: ")
Priority = input("Enter the task priority (high/medium/low): ").lower()
Time_Bound = input("Is this task time-bound? (yes/no): ").lower()

# Process the task using match-case based on priority
match Priority:
    case "high":
        reminder = f"Your task: '{Task}' is HIGH priority."
    case "medium":
        reminder = f"Your task: '{Task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task: '{Task}' is LOW priority."
    case _:
        reminder = f"Your task: '{Task}' has an UNKNOWN priority."

# Modify reminder if the task is time-sensitive
if Time_Bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)