import random

def calc_pi(num):

    numberOfHits = 0

    for i in range(num):
        x = random.random()*2 -1
        y = random.random()*2 -1

        if x * x + y * y <=1:
            numberOfHits +=1
    
    return 4* numberOfHits / num

print("PI is", calc_pi(10000))