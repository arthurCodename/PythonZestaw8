def P_recursive(i, j):
    if i == 0 and j == 0:
        return 0.5

    elif i > 0 and j == 0:
        return 0.0

    elif i == 0 and j > 0:
        return 1.0
    
    elif i > 0 and j > 0:
        return  0.5 * (P_recursive(i-1, j) + P_recursive(i, j-1)) 

print(P_recursive(10, 12))


