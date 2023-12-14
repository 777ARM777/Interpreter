from validators import *
from variables import *
from my_types import *
from evaluate_expression import *


def decl_function(code: str) -> int:
    """For variable declaration"""
    scopes[-1][code[2]] = eval(f'{code[1].capitalize()}')(code[2], code[4])
    return 0

def read_function(code: str) -> int:
    """Input function"""

    var = get_variable(code[1])
    T = eval(var.__class__.__name__)
    value = input('Input value: ')
    if var.__class__.__name__ == 'String':
        value = '"' + value + '"'
    if not eval(f'{(var.__class__.__name__).lower()}_validator')(value):
        raise ValueError(f'Invalid literal {value} for type {code[1]}')

    value = T(code[1], value)
    scope_index = get_variable_scope(code[1])
    scopes[scope_index][code[1]] = value
    return 0


def display_function(code: str) -> int:
    """Print function"""
    if len(code) > 2:
        expression = infix_to_postfix(' '.join(code[1:]))
        print(evaluate_postfix(expression))
    elif is_literal(code[1]):
        print(code[1])
    else:
        print(get_variable(code[1]))
    return 0


def assignment_function(code: str) -> int:
    """For expressions"""
    postfix = infix_to_postfix(' '.join(code[2:]))
    T = eval(get_variable(code[0]).__class__.__name__)
    value = T(code[0], evaluate_postfix(postfix))

    scope_index = get_variable_scope(code[0])
    scopes[scope_index][code[0]] = value
    return 0




def check_function(code: str) -> int:
    """If statement"""
    for i in range(len(code)):
        if is_operator(code[i]):
            expression_validator(' '.join(code[1:i]))
            expression_validator(' '.join(code[i + 1:-1]))

            postfix = infix_to_postfix(' '.join(code[1:i]))
            left_value = evaluate_postfix(postfix)

            postfix = infix_to_postfix(' '.join(code[i + 1:-1]))
            right_value = evaluate_postfix(postfix)
            value = eval(f'{left_value} {code[i]} {right_value}')

            if value:
                return 1
            else:
                return 2








def other_function(code: str) -> bool:
    """Else statement"""
    ...


def step_function(code: str) -> bool:
    """For statement"""
    ...


def till_function(code: str) -> bool:
    """While statement"""
    ...
