from validators import *
from variables import *
from my_types import *
from evaluate_expression import *


def decl_function(code: str) -> None:
    """For variable declaration"""
    global_vars[code[2]] = eval(f'{code[1].capitalize()}')(code[2], code[4])


def read_function(code: str) -> None:
    """Input function"""

    T = eval(global_vars[code[1]].__class__.__name__)
    value = input('Input value: ')

    if not eval(f'{(global_vars[code[1]].__class__.__name__).lower()}_validator')(value):
        raise ValueError(f'Invalid literal {value} for type {code[1]}')

    value = T(code[1], value)
    global_vars[code[1]] = value


def display_function(code: str) -> None:
    """Print function"""
    if len(code) > 2:
        expression = infix_to_postfix(' '.join(code[1:]))
        print(evaluate_postfix(expression))
    elif is_literal(code[1]):
        print(code[1])
    else:
        print(global_vars[code[1]])


def assignment_function(code: str) -> None:
    """For expressions"""
    postfix = infix_to_postfix(' '.join(code[2:]))
    T = eval(global_vars[code[0]].__class__.__name__)
    value = T(code[0], evaluate_postfix(postfix))
    global_vars[code[0]] = value


def check_function(code: str) -> None:
    """If statement"""
    ...


def other_function(code: str) -> None:
    """Else statement"""
    ...


def step_function(code: str) -> None:
    """For statement"""
    ...


def till_function(code: str) -> None:
    """While statement"""
    ...
