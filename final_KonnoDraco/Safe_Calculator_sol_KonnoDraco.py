def safe_calculate(num1, num2, operation):
    """
    Perform arithmetic operation with exception handling.
    Parameters:
    num1: First number (can be string or number)
    num2: Second number (can be string or number)
    operation (str): One of '+', '-', '*', '/'
    Returns:
    float: Result of the operation
    str: Error message if operation fails
    Examples:
    safe_calculate(10, 5, '+') returns 15.0
    safe_calculate("10", "5", '-') returns 5.0
    safe_calculate(10, 0, '/') returns "Error: Division by zero"
    safe_calculate("abc", 5, '+') returns "Error: Invalid number"
    safe_calculate(10, 5, '%') returns "Error: Invalid operation"
    """
    # YOUR CODE HERE
    # Step 1: Try to convert num1 and num2 to float
    # Step 2: Check if operation is valid (+, -, *, /)
    # Step 3: Perform the operation
    # Step 4: Handle division by zero
    # Step 5: Handle invalid number conversion
    try:
        # Convert inputs to numbers
        # Check operation and calculate
        num1 = float(num1)
        num2 = float(num2)
        
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
        else:
            return "Error: Invalid Operation"
    except ValueError:
        return "Error: Invalid Number"
    except ZeroDivisionError:
        return "Error: Division by Zero"
# Test your function:
print(safe_calculate(10, 5, '+')) # 15.0
print(safe_calculate("10", "5", '-')) # 5.0
print(safe_calculate(10, 0, '/')) # Error: Division by zero
print(safe_calculate("abc", 5, '+')) # Error: Invalid number