from interprete_functions import *

if __name__ == '__main__':
    # Reading file
    with open('code.my') as code:
        code = code.readlines()

    # Syntax analyze and run code
    i = 0
    count = 0
    condition_stack = Stack()
    # print(condition_stack.items)
    while i < len(code):
        # print(code[i][:-1])
        code[i] = code[i].strip()

        # for s in scopes:
        #     print(s)
        # print()
        if code[i].startswith('}'):                     # End of scope
            scopes.pop()
            if condition_stack.top()[1]:
                condition_stack.pop()
                count -= 1

        elif code[i].startswith('other'):               # else case
            if not condition_stack.top()[0]:
                raise SyntaxError('Other without Check')
            # print(i + 1, code[i])
            scopes.append({})
            if condition_stack.top()[1]:                         # if else case then does this
                count += 1
                i += 1
                continue
            else:                                       # if not else case then passes else
                while i < len(code) - 1:
                    i += 1
                    # print(i, code[i])
                    code[i] = code[i].strip().split(' ')
                    if code[i][0] in ('check', 'other', 'step', 'till'):
                        count += 1

                    if code[i][0].startswith('}'):
                        if count == 0:
                            condition_stack.pop()
                            # print(i + 1, code[i])
                            scopes.pop()
                            break
                        else:
                            count -= 1
                # print(i + 1, code[i])
                # scopes.pop()

        else:
            code[i] = analyze_code(code[i])
            a = run_line(code[i])

            if a == 1 or a == 2:
                condition_stack.push([True, False])
                scopes.append({})

            if a == 2:
                condition_stack.top()[1] = True
                count = 0
                while i < len(code):
                    i += 1
                    code[i] = code[i].strip().split(' ')

                    if code[i][0] in ('check', 'other', 'step', 'till'):
                        count += 1

                    if code[i][0] == '}' or code[i][0] == '}\n':
                        if count == 0:
                            # print(i + 1, code[i])
                            scopes.pop()
                            break
                        else:
                            count -= 1
                # print(i + 1, code[i])
                # scopes.pop()


        i += 1
