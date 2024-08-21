def ReversePolishNotation(strParam):
    
    stack = []  # create an empty list to locally store data
    
    content = strParam.split()    # split the input string at spaces
    
    # Iterate through each token in the expression
    for token in content:
        if token.isdigit():
            # If the token is a digit, append it to stack
            stack.append(int(token))
        else:
            # Otherwise it is an operator
            operand2 = stack.pop()      # remove the last element of stack and take it as second operand
            operand1 = stack.pop()      # remove the last element of stack and take is as first operand
            
            # Perform the operation
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
            else:
                raise ValueError(f"Non standard Polish notation")
    
    # The final result will be the only item left on the stack
    return stack.pop()
