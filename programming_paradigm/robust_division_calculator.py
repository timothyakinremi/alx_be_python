def safe_divide(numerator, denominator):
    # Safely dividing two numbers with error handling.
    
    try:
        num = float(numerator)
        den = float(denominator)
        
        # Perform division operation
        result = num/den
        return f"The result of dividing {num} by {den} is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Please provide numeric values for numerator and denominator."