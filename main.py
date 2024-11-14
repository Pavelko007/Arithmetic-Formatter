def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    for problem in problems:
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        
        left, op, right = problem.split()

        if not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        width = max(len(left), len(right)) + 2
        line1.append(left.rjust(width))
        line2.append(op + right.rjust(width - 1))
        line3.append('-' * width)
        line4.append(str(eval(problem)).rjust(width))
    
    lines = [line1, line2, line3]
    if show_answers:
        lines.append(line4)

    arranged_problems = '\n'.join(['    '.join(line) for line in lines])
    return arranged_problems


print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
# print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')