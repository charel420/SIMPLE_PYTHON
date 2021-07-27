def solve_for_x(equation):
    
    x = -3000 #works only if equation is higher than x
    new_eq = equation.replace("=", "==")
    
    
    if eval(new_eq):
        return 0
    else:
        while eval(new_eq) is False:
            x += 1
    
    return x
