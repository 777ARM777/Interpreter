from variables import *
from validators import *


def decl_analyze(code: list) -> list:
    """For variable declaration analyze"""
    # print(code)
    if len(code) != 5:
        raise SyntaxError('Invalid expression')

    if not code[1] in type_names:
        raise TypeError(f'{code[1]} does not a name of type')

    if not identifier_name_validator(code[2]):
        raise NameError(f'Invalid name of variable {code[2]}')

    if code[3] != '=':
        raise SyntaxError('Invalid expression')

    if is_literal(code[4]) and not eval(f'{code[1]}_validator')(code[4]):
        if not identifier_name_validator(code[4]):
            raise NameError(f'Invalid name of variable {code[4]}')

        if code[4] not in keywords:
            raise NameError(f'{code[4]} is not defined')

        raise ValueError(f'Invalid literal {code[4]} for type {code[1]}')



    return code

def read_analyze(code: list) -> list:
    """Input analyze"""

    if len(code) != 2:
        raise SyntaxError('Invalid expression for reading variable')

    if code[1] not in global_vars:
        raise NameError(f'Invalid name of variable {code[1]}')

    return code


def display_analyze(code: list) -> list:
    """Print analyze"""

    if len(code) < 2:
            raise SyntaxError('Invalid expression for displaying element')

    if not is_literal(code[1]):
        if code[1] not in global_vars:
            raise NameError(f'Invalid name of variable {code[1]}')

    return code


def assignment_analyze(code: list) -> list:
    """For expressions analyze"""
    if code[0] not in global_vars:
        raise NameError(f'Invalid name of variable {code[0]}')
    if code[1] != '=':
        raise SyntaxError('Invalid expression')

    expression_validator(' '.join(code[2:]))  #TODO

    return code


def check_analyze(code: list) -> list:
    """If statement analyze"""
    ...


def other_analyze(code: list) -> list:
    """Else statement analyze"""
    ...


def step_analyze(code: list) -> list:
    """For statement analyze"""
    ...


def till_analyze(code: list) -> list:
    """While statement analyze"""
    ...
