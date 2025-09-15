# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"REMINDER: '{task}' is HIGH priority task"
    case "medium":
        reminder = f"REMINDER: '{task}' is MEDIUM priority task"
    case "low":
        reminder = f"REMINDER: '{task}' is LOW priority task"
    case _:
        reminder = f"Your task: '{task}' has an UNKNOWN priority"

if time_bound == 'yes':
    reminder += " that requires immediate action."
    print(reminder)

else:

    print(f"Note: '{task}' is a '{priority}' priority task. Consider completing it when you have free time.")
