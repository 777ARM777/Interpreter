from validators import *
from variables import *
from my_types import *
from evaluate_expression import *


def decl_function(code: list) -> int:
    """For variable declaration"""
    scopes[-1][code[2]] = eval(f'{code[1].capitalize()}')(code[2], code[4])
    return 0

def read_function(code: list) -> int:
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


def display_function(code: list) -> int:
    """Print function"""

    if len(code) > 2:
        expression = infix_to_postfix(' '.join(code[1:]))
        print(evaluate_postfix(expression))
    elif is_literal(code[1]):
        print(code[1])
    else:
        print(get_variable(code[1]))

    return 0


def assignment_function(code: list) -> int:
    """For expressions"""

    postfix = infix_to_postfix(' '.join(code[2:]))
    T = eval(get_variable(code[0]).__class__.__name__)

    scope_index = get_variable_scope(code[0])
    value = T(code[0], evaluate_postfix(postfix))
    op = code[1]

    if op != '=':
        value = calculate(scopes[scope_index][code[0]], value, op[:-1])

    scopes[scope_index][code[0]] = value

    return 0


def check_function(code: list) -> int:
    """If statement"""
    for i in range(len(code)):
        if is_condition_operator(code[i]):
            expression_validator(' '.join(code[1:i]))
            expression_validator(' '.join(code[i + 1:-1]))

            postfix = infix_to_postfix(' '.join(code[1:i]))
            left_value = evaluate_postfix(postfix)

            postfix = infix_to_postfix(' '.join(code[i + 1:]))
            right_value = evaluate_postfix(postfix)

            condition = f'{left_value} {code[i]} {right_value}'
            value = eval(condition)

            if value:
                return 1
            else:
                return 2


def other_function(code: list) -> int:   # TODO
    """Else statement"""
    ...


def step_function(code: list) -> int:
    """For statement"""
    index1 = code.index(':')
    index2 = code.index(':', index1 + 1)

    assignment_function(code[2:index1])

    check = check_function(['check'] + code[index1 + 1: index2])

    if check == 1:
        return 3
    else:
        return 2

def till_function(code: list) -> int:
    """While statement"""
    check = check_function(['check'] + code[2:-2])

    if check == 1:
        return 4
    else:
        return 2