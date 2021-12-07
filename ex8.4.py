import math

def heron(a, b, c):
    arr = [a, b, c]
    arr.sort()
    if arr[2] > arr[0] + arr[1]:
        raise ValueError("No")
    else: 
        halfparam = (a + b + c) / 2
        return math.sqrt(halfparam * (halfparam - a) * (halfparam - b) * (halfparam - c))


print(heron(5, 3.5,4.5))