def arithmetic_arranger(problems, solve_problem=False):
    # error handling
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        try:
            operand1, operator, operand2 = problem.split(' ')
        except:
            return "Error: Invalid problem format."
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        try:
            operand1 = int(operand1)
            operand2 = int(operand2)
        except:
            return "Error: Numbers must only contain digits."
        if operand1 > 9999 or operand2 > 9999:
            return "Error: Numbers cannot be more than four digits."

    top_line = []
    bottom_line = []
    dash_line = []
    result_line = []
    for problem in problems:
        # could be done while error handling. But let's keep it separated for readability
        operand1, operator, operand2 = problem.split(' ')
        if len(operand1) > len(operand2):
            arranged_problems_len = len(operand1)
        else:
            arranged_problems_len = len(operand2)
        if solve_problem:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            # arranged_problems_len+2 to add room for operator and space
            result_line.append(f"{str(result).rjust(arranged_problems_len+2)}")
        top_line.append(f'{operand1.rjust(arranged_problems_len + 2)}')
        bottom_line.append(f'{operator} {operand2.rjust(arranged_problems_len)}')
        dash_line.append(f'{"".rjust(arranged_problems_len+2, "-")}')
    top_line = '    '.join(top_line)
    bottom_line = '    '.join(bottom_line)
    dash_line = '    '.join(dash_line)
    arranged_problems = '\n'.join([top_line, bottom_line, dash_line])
    if solve_problem:
        result_line = '    '.join(result_line)
        arranged_problems = f'{arranged_problems}\n{result_line}'
    return arranged_problems


if __name__ == "__main__":
    print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))
