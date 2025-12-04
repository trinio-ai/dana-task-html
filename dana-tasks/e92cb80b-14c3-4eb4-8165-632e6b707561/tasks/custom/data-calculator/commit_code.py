"""
Commit code for Data Calculator task.

This code runs when the user submits the form. It performs the calculation
and returns the result.

Note: The sandbox environment has restricted builtins.
Only basic types and operations are allowed (no imports, no exceptions).
Use commit_result with 'error' status for error handling.
"""

# Get form data
number_a = float(form_data.get('number_a', 0))
number_b = float(form_data.get('number_b', 0))
operation = form_data.get('operation', 'add')

# Initialize result
result = None
op_symbol = ''
error_message = None

# Perform calculation
if operation == 'add':
    result = number_a + number_b
    op_symbol = '+'
elif operation == 'subtract':
    result = number_a - number_b
    op_symbol = '-'
elif operation == 'multiply':
    result = number_a * number_b
    op_symbol = '*'
elif operation == 'divide':
    if number_b == 0:
        error_message = "Cannot divide by zero"
    else:
        result = number_a / number_b
        op_symbol = '/'
else:
    error_message = "Unknown operation: " + str(operation)

# Return result
if error_message:
    commit_result = {
        "status": "error",
        "error": error_message,
        "inputs": {
            "number_a": number_a,
            "number_b": number_b,
            "operation": operation
        }
    }
else:
    expression = str(number_a) + " " + op_symbol + " " + str(number_b) + " = " + str(result)
    commit_result = {
        "status": "success",
        "result": result,
        "expression": expression,
        "inputs": {
            "number_a": number_a,
            "number_b": number_b,
            "operation": operation
        }
    }
