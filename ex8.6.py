def P_recursive(i, j):
    if i == 0 and j == 0:
        return 0.5

    elif i > 0 and j == 0:
        return 0.0

    elif i == 0 and j > 0:
        return 1.0
    
    elif i > 0 and j > 0:
        return  0.5 * (P_recursive(i-1, j) + P_recursive(i, j-1)) 

print(P_recursive(12, 0))

def P_dynamic(i,j):
    dict = {}
    dict[0,0] = 0.5
    
    for x in range(1,i+1):
        dict[x, 0] = 0
    for y in range(1,j+1):
        dict[0, y]= 1
    for x in range(1,i+1):
        for y in range(1,j+1):
            dict[x, y] = 0.5 * (dict[x-1, y] + dict[x, y-1])

    return dict[i,j]


print(P_dynamic(12, 0))


