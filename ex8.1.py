def solve1(a,b,c):
    if a == 0 and b != 0:
       return 'Y is equal to {}'.format( -c/b)

    elif a!=0 and b ==0:
       return 'X is equal to {}'. format(-c/a)

    elif a != 0 and b != 0:
        return 'The solution can be any number'

    elif a == 0 and b ==0:
        return 'Not viable equation'
        
    elif(a == 0 and b == 0 and c == 0):
        print("An equation has infinitely many solutions")

    elif(a == 0 and b == 0 and c != 0):
        print("Conflicting equation")



