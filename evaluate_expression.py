from stack import Stack
from validators import *
from my_types import *
import re

def is_operator(c):
    return c in operators


def is_operand(c):
    return not is_operator(c)


def infix_to_postfix(infix: str) -> str:
    """Converts expression from infix to postfix"""
    # print('Infix: ', infix)

    postfix = ""
    stack = Stack()

    def priority(c):
        if c in ['+', '-']:
            return 0
        elif c in ['*', '/']:
            return 1
        elif c == '^':
            return 2
        return -1

    for i in infix:
        if i == '(':
            stack.push('(')

        elif i == ')':
            while not stack.is_empty() and stack.top() != '(':
                postfix += ' ' + stack.top()
                stack.pop()
            if not stack.is_empty():
                stack.pop()
            else:
                return ""

        elif is_operand(i):
            postfix += i

        elif is_operator(i):
            while not stack.is_empty() and is_operator(stack.top()) and priority(stack.top()) >= priority(i):
                postfix += ' ' + stack.top()
                stack.pop()
            stack.push(i)


        else:
            return ""

    while not stack.is_empty():
        postfix += ' ' + stack.top()
        stack.pop()

    return postfix.strip()


def evaluate_postfix(postfix: str) -> any:
    # print('Postfix: ', postfix)
    postfix = re.findall(r'"[^"]*"|\S+', postfix)
    stack = Stack()

    def calculate(operand1, operand2, op):
        expression = f"{operand1} {op} {operand2}"
        T = eval(typeof(operand1))
        return T('a', eval(expression))

    for i in range(len(postfix)):
        if is_operand(postfix[i]):
            if is_literal(postfix[i]):
                tmp = eval(typeof(postfix[i]))
                stack.push(tmp('a', postfix[i]))
            var =  get_variable(postfix[i])
            if var:
                stack.push(var)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.push(calculate(operand1, operand2, postfix[i]))
    return stack.top()
