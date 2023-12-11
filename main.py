from interprete_functions import *

if __name__ == '__main__':
    # Reading file
    with open('code.my') as code:
        code = code.readlines()

    # Syntax analyze and run code
    for i in range(len(code)):
        code[i] = code[i].strip()
        code[i] = analyze_code(code[i])
        run_line(code[i])
