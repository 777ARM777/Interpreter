from analyze_functions import *
from run_functions import *
from variables import *
from my_types import *


def run_line(code: str) -> list:
    if code is None:
        return []
    if code[0] in keywords:
        func = eval(f'{code[0]}_function')
        code = func(code)
        return code
    assignment_function(code)

def analyze_code(code):
    if not code:
        return

    # Split code
    is_str = False
    res = ['']
    for i in code:
        if i == ' ' and not is_str:
            res.append('')
        elif i == "'" or i == '"':
            res[-1] += '"'
            is_str = not is_str
        else:
            res[-1] += i
    # print(res)

    for keyword in keywords:
        if res[0] == keyword:
            func = eval(f'{keyword}_analyze')
            res = func(res)
            return res
    return assignment_analyze(res)