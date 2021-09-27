import re

def operatorRe(operators): #arr->re with or between every operator
    return '(?:'+'|'.join(operators)+')'

float_re=r'\s*?[\d|\.]+\s*?'
operators=[['\\*\\*', '\\^'], ['\\*', '\\/'], ['\\+', '\\-']] #grouped into arrays of operators that are equal so they are evaluated at same time (will be prepended by )
single_dimension_operators=[]
for sub_operators in operators:
    for operator in sub_operators:
        single_dimension_operators.append(operator)

all_expressions_re=operatorRe(single_dimension_operators)

print(all_expressions_re)
def calc_one_equation(str):
    expressionRe=f'({float_re})({all_expressions_re})({float_re})'
    print(expressionRe)
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
    elif operator=='ab' or operator=='^':
        return first_num**second_num
    else:
        print('Error, operator not recognized.')

def calc_many_equations(raw_user_input):
    ans=raw_user_input

    parentheses=re.match('\\('+all_expressions_re+'\\)')
    

    for sub_operators in operators:
        operator_specific_re=operatorRe(sub_operators)
        searched=re.search(operator_specific_re, ans)
        print(operator_specific_re)
        print(searched)
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
    if raw_user_input=='config':
        print('__Config__')
    print(calc_many_equations(raw_user_input))

print('Goodbye')