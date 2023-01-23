def balance( arr ):
    temp = []
    d1 = ['(', ')', '{', '}', '[', ']' ]
    for i in arr:
        if(i in d1): # I removed operands and operators and only kept parentheses
            temp.append(temp) 

    d2 = {'(' : ')', '[' : ']', '{' : '}' } 
    stack = []
    for j in temp:
        if(j in d2):
            stack.append(j)
        elif(len(stack) == 0 or d2[stack.pop()] != j):
            return False
    return len(stack) == 0