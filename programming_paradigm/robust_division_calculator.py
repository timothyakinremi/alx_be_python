def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling.
    
    Args:
        numerator: The number to be divided (int, float, or numeric string).
        denominator: The number to divide by (int, float, or numeric string).
    
    Returns:
        str: A formatted message showing the division result or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
