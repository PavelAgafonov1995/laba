def calculate(input_string):
    try:
        stack = [];
        for operand in input_string.rsplit():
            if operand not in '+-*/':
                stack.append(operand);
            else:
                op2 = stack.pop();
                op1 = stack.pop();
                expression = op1 + operand + op2;
                result = eval(expression);
                stack.append(str(result));
            
        result = stack.pop();
        if len(stack) == 0:
            return result;
        else:
            raise Exception ('Ошибка');
            
    except Exception as e :
        
        raise Exception ('Ошибка');



input_string = input();
try:
    print (calculate(input_string));
except Exception as e:
    print (e)
