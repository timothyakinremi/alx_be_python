# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    """Main function to handle user input and temperature conversion."""
    try:
        temperature = float(input("Enter the temperature value: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()

