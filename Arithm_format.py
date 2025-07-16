def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first_lines = []
    second_lines = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts

        # Error handling
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        #Format
        width = max((len(operand1)), len(operand2)) + 2
        line1 = " " * (width - len(operand1)) + operand1
        line2 = operator + " " * (width - 1 - len(operand2)) + operand2
        line3 = "-" * width

        if show_answers:
            if operator == "+":
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
        #append
            line4 = " " * (width - len(result)) + result
            answers.append(line4)

        first_lines.append(line1)
        second_lines.append(line2)
        dashes.append(line3)

    # Join lines
    arranged = '    '.join(first_lines) + '\n' + \
               '    '.join(second_lines) + '\n' + \
               '    '.join(dashes)
    
    if show_answers:
        arranged += '\n' + '    '.join(answers)

    return arranged
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))