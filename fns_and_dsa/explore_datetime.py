from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # return current_date so we can reuse it in the next function


def calculate_future_date(current_date):
    """Calculate and display a future date after a specified number of days."""
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("⚠️ Please enter a valid integer for the number of days.")


def main():
    """Main function to execute datetime operations."""
    current_date = display_current_datetime()
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
