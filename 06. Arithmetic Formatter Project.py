def arithmetic_arranger(problems, display_answers=False):
    # Validation
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts

        # Error checks
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Formatting: width is max length + 2 (one for operator, one padding)
        width = max(len(num1), len(num2)) + 2

        # Right-align first operand in width
        first_line.append(num1.rjust(width))

        # Operator + right-aligned second operand in (width - 1) because operator uses 1 char
        second_line.append(operator + num2.rjust(width - 1))

        # Dash line exactly width dashes
        dashes.append('-' * width)

        # Optional results: compute and rjust to same width
        if display_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(width))

    # Join with four spaces between problems
    arranged = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    if display_answers:
        arranged += '\n' + '    '.join(results)

    return arranged