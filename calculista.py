import re

float_re=r'\s*?[\d|\.]+\s*?'

def operatorRe(operators): #arr->re with or between every operator
    return '(?:'+'|'.join(operators)+')'

operators=[['\\*\\*', '\\^'], ['\\*', '\\/'], ['\\+', '\\-']] #grouped into arrays of operators that are equal so they are evaluated at same time (will be prepended by )
single_dimension_operators=[]
for sub_operators in operators:
    for operator in sub_operators:
        single_dimension_operators.append(operator)

all_expressions_re=operatorRe(single_dimension_operators)

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

factorial_re=fr'({float_re}\!)'

def calc_factorial(str):
    matched_int=int(re.match(fr'({float_re})\!', str).groups()[0]) #extract int from {int}!
    product=1
    while(matched_int>1):
        product*=matched_int
        matched_int-=1
    return product

parentheses_re=fr'\(\s*?(.*)\s*?\)'

def calc_many_equations(raw_user_input):
    ans=raw_user_input

    #parantheses
    parentheses_res=re.search(parentheses_re, ans)
    while parentheses_res is not None:
        start_i=parentheses_res.start()
        end_i=parentheses_res.end()
        ans=ans[0:start_i]+str(calc_many_equations(parentheses_res.groups()[0]))+ans[end_i:] #calculate stuff inside parantheses
        parentheses_res=re.search(parentheses_re, ans)


    #check for factorial
    factorial_res=re.search(factorial_re, ans)
    while factorial_res is not None:
        start_i=factorial_res.start()
        end_i=factorial_res.end()
        ans=ans[0:start_i]+str(calc_factorial(factorial_res.groups()[0]))+ans[end_i:]
        factorial_res=re.search(factorial_re, ans)
    
    
    #operators
    for sub_operators in operators:
        operator_specific_re=float_re+operatorRe(sub_operators)+float_re
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
    if raw_user_input=='config':
        print('__Config__')
    print(calc_many_equations(raw_user_input)) #print result

print('Goodbye')