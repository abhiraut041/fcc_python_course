# FCC First Course Project (Dec 6th, 2024)

def arithmetic_arranger(problems, show_answers=False):
    problem_limit = 5
    if len(problems) > 5:
        return 'Error: Too many problems.'
    answer_str = ""
    
    for idx in range(len(problems)):
        # split the inputs
        arg1, op, arg2 = problems[idx].split(' ')
        # Check constraints and solve if speciifed 
        if op not in '+-':
            return 'Error: Operator must be \'+\' or \'-\'.'
        if not arg1.isdigit() or not arg2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if int(arg1) > 9999 or int(arg2) > 9999:
            return 'Error: Numbers cannot be more than four digits.'
        
        # pad the strings as per the max length
        mx_len = max(len(arg1), len(arg2))
        arg1 = arg1.rjust(mx_len,' ')
        arg2 = arg2.rjust(mx_len,' ')
        dotted_line = '-' * (mx_len+2)
        # modify the problem to help in formatting
        problems[idx] = (arg1, op, arg2, dotted_line)
    
    # Format the answer string
    total_lines = 4 if show_answers else 3
    mid_space = ' '*4
    start_space = ' '*2
    for line_num in range(total_lines):
        line = ""
        for problem in problems:
            # print arg1
            if line_num == 0:
                line += start_space+problem[0]+mid_space
            # print op and arg2
            if line_num == 1:
                line += problem[1]+' '+problem[2]+mid_space
            # print dotted-line
            if line_num == 2:
                line += problem[3]+mid_space
            # print solution if asked
            if line_num == 3:
                a, op, b = int(problem[0]), problem[1], int(problem[2])
                res = a+b if op == '+' else a-b
                line += str(res).rjust(len(problem[3])) + mid_space
        answer_str += line.rstrip()
        if line_num != total_lines-1:
            answer_str += '\n'
    
    return answer_str
    
# solution = arithmetic_arranger(["9999 + 6998", "3801 - 2", "45 + 43", "123 + 49"])
solution = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
print(solution)