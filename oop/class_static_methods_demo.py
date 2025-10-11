# class_static_methods_demo.py

class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: performs addition of two numbers.
        Does not depend on the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: performs multiplication and accesses class-level data.
        Prints the calculation type before performing the operation.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")
