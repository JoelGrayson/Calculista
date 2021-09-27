import re

def calc_many_equations(raw_user_input):
    ans=raw_user_input

    float_re=r'\s*?[\d|\.]+\s*?'
    operators=[['**', '^'], ['*', '/'], ['+', '-']] #grouped into arrays of operators that are equal so they are evaluated at same time (will be prepended by )
    all_expressions_re='[' #formats expression into [regex|or]
    for operator_arr in operators:
        for operator in operator_arr:
            all_expressions_re+='|\\'+operator
    all_expressions_re+=']'

    def calc_one_equation(str):
        expressionRe=f'({float_re})({all_expressions_re})({float_re})'
        groups=re.search(expressionRe, str).groups()
        first_num=float(groups[0])
        operator=groups[1]
        second_num=float(groups[2])
        if operator=='*':
            return first_num*second_num
        elif operator=='/':
            return first_num/second_num 
        elif operator=='+':
            return first_num+second_num 
        elif operator=='-':
            return first_num-second_num
        elif operator=='**' or operator=='^':
            return first_num**second_num
        else:
            print('Error, operator not recognized.')
    
    for sub_operators in operators:
        operator_specific_re=float_re+'['+'|\\'.join(sub_operators)+']'+float_re
        searched=re.search(operator_specific_re, ans)
        while searched is not None:
            operator_occurrence=re.search(operator_specific_re, ans)
            start=operator_occurrence.start()
            end=operator_occurrence.end()
            ans=ans[0:start]+str(calc_one_equation(ans[start:end]))+ans[end:]
            searched=re.search(operator_specific_re, ans)
    return ans

print('__The Joelavid Calculator__')
print('Enter an equation or \'q\' to quit\n')

while True:
    raw_user_input=input('> ').lower().strip()
    if raw_user_input=='q':
        break
    print(calc_many_equations(raw_user_input))

print('Goodbye')