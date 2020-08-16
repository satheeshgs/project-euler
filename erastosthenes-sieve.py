def sieveoferatosthenes(n):
    #boolean array creation with all values initialized to 1
    prime=[True for i in range(n+1)]
    #set the first prime number to a variable p
    p=2
    #define the terminating condition (p*p <=n)
    while(p*p<=n):
        #starting the iterations and updating multiples
        if(prime[p]==True):
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    prime[0]=False
    prime[1]=False
    primearr=[]

    for p in range(n+1):
        if(prime[p]==True):
            primearr.append(p)

    #return the prime array values
    return(primearr)


arr=sieveoferatosthenes(2000000)
sum(arr)
