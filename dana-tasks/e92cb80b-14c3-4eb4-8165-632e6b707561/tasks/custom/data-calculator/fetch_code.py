"""
Fetch code for Data Calculator task.

This code runs when the task form is loaded to provide default values
and dropdown options.
"""

# Get any pre-filled values from input parameters
preset_a = input_parameters.get('number_a', 0)
preset_b = input_parameters.get('number_b', 0)
preset_op = input_parameters.get('operation', 'add')

# Provide default values and available operations
fetched_data = {
    "defaults": {
        "number_a": preset_a,
        "number_b": preset_b,
        "operation": preset_op
    },
    "operations": [
        {"value": "add", "label": "Add (+)"},
        {"value": "subtract", "label": "Subtract (-)"},
        {"value": "multiply", "label": "Multiply (*)"},
        {"value": "divide", "label": "Divide (/)"}
    ],
    "message": "Data Calculator is ready. Enter two numbers and select an operation."
}
