def isprime(num):
    for i in range(2,num-1):
        if(num==2):
            return True
        elif(num%i==0):
            break
    else:
        return True

def findnextprime(num):
    prime =num
    i=1
    while(i==1):
        prime=prime+1
        if(isprime(prime)==True):
            return(prime)
            i=0
p=2
i=1
while(i<10001):
    p=findnextprime(p)
    i=i+1

print(p)
