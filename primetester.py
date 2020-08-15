import math
def isprime(n):
    if(n==1):
        return False
    elif(n<4):
        return True
    elif(n%2==0):
        return False
    elif(n<9):
        return True
    elif(n%3==0):
        return False
    else:
        r=floor(math.sqrt(n))
        f=5
        while(f<=r):
            if(n%f==0):
                return False
                break
            if(n%(f+2)==0):
                return False
                break
            f=f+6
        return True


isprime(13)
