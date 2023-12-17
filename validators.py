import re
from variables import *

def is_literal(value: str) -> bool:
    if value == 'true' or value == 'false':
        return True

    if value[0].isdigit():
        return True

    if value[0] == '"':
        return True

def is_condition_operator(value: str) -> bool:
    return value in condition_operators

def typeof(value: any):
    var = get_variable(value)
    if var:
        return var.__class__.__name__
    if isinstance(value, str):
        if integer_validator(value):
            return 'Integer'
        if double_validator(value):
            return 'Double'
        if string_validator(value):
            return 'String'
        if boolean_validator(value):
            return 'Boolean'

    if value.__class__.__name__.lower() in type_names:
        return value.__class__.__name__

    raise ValueError(f'{value} is not a literal or valid variable.')

def get_variable(var: str):
    for i in range(len(scopes) - 1, -1, -1):
        if var in scopes[i]:
            return scopes[i][var]

    return None

def get_variable_scope(var: str):
    for i in range(len(scopes) - 1, -1, -1):
        if var in scopes[i]:
            return i

    return None


def identifier_name_validator(identifier: str) -> bool:
    # Define the regex pattern for a valid Python identifier
    if identifier in keywords:
        return False

    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    match = pattern.match(identifier)
    return bool(match)


def literal_validator(value: str) -> bool:
    if integer_validator(value) or double_validator(value) or boolean_validator(value) or string_validator(value):
        return True
    return False

def integer_validator(input_string):
    # Define the regex pattern for integer validation
    pattern = re.compile(r'^[+-]?\d+$')

    # Match the pattern against the input string
    match = pattern.match(input_string)

    # Check if the string is a valid integer
    if match:
        return True
    else:
        return False


def double_validator(input_string):
    # Define the regex pattern for double validation
    pattern = re.compile(r'^[+-]?\d+(\.\d+)?$')

    # Match the pattern against the input string
    match = pattern.match(input_string)

    # Check if the string is a valid double
    if match:
        return True
    else:
        return False


def boolean_validator(input_string):
    if input_string in ('true', 'false'):
        return True
    return False


def string_validator(input_string):
    # Define the regex pattern for a string enclosed in single quotes
    pattern = re.compile(r'^[\'\"](.*?)[\'\"]$')

    # Match the pattern against the input string
    match = pattern.match(input_string)

    # Check if the string is valid
    if match:
        return True
    else:
        return False


def expression_validator(expression) -> bool:  # TODO
    pass

def condition_validator(code: str) -> bool:  # TODO
    pass