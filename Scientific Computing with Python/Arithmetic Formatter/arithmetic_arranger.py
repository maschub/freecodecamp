def arithmetic_arranger(problems, solve_problem = False):
    # error handling
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        try:
            value1, operand, value2 = problem.split(' ')
        except:
            return "Error: Invalid problem format."
        if operand not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        try:
            value1 = int(value1)
            value2 = int(value2)
        except:
            return "Error: Numbers must only contain digits."
        if value1 > 9999 or value2 > 9999:
            return "Error: Numbers cannot be more than four digits."

    arranged_problems = "first_line\nsecond_line\ndash_line\nresult_line"
    for problem in problems:
        # could be done while error handling. But would not be that pretty
        value1, operand, value2 = problem.split(' ')
        if len(value1) > len(value2):
            arranged_problems_len = len(value1)
        else:
            arranged_problems_len = len(value2)
        result = ""
        if solve_problem:
            if operand == '+':
                result = int(value1) + int(value2)
            else:
                result = int(value1) - int(value2)
            # arranged_problems_len+2 to add room for operand and space
            result = f"{str(result).rjust(arranged_problems_len+2)}"
        arranged_problems = arranged_problems.replace(
            'first_line', f'{value1.rjust(arranged_problems_len + 2)}    first_line'
        )
        arranged_problems = arranged_problems.replace(
            'second_line', f'{operand} {value2.rjust(arranged_problems_len)}    second_line'
        )
        arranged_problems = arranged_problems.replace(
            'dash_line', f'{"".rjust(arranged_problems_len+2, "-")}    dash_line'
        )
        arranged_problems = arranged_problems.replace(
            'result_line', f'{result}    result_line'
        )
    arranged_problems = arranged_problems.replace(
        '    first_line', ''
    )
    arranged_problems = arranged_problems.replace(
        '    second_line', ''
    )
    if not solve_problem:
        arranged_problems = arranged_problems.replace(
            '    dash_line\n    ', ''
        )
    else:
        arranged_problems = arranged_problems.replace(
            '    dash_line', ''
        )
    arranged_problems = arranged_problems.replace(
        '    result_line', ''
    )
    arranged_problems = arranged_problems.rstrip()

    return arranged_problems

if __name__ == "__main__":
    print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))