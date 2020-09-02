def isprime(num):
    c=0
    for i in range(2,num):
        if num%i==0:
            c+=1
            break
    if c==0:
        return True
    else:
        return False

n=1
c=0
while n>0:
    n+=1
    if isprime(n):
        c+=1
        print("DEBUG C ",c)
        print("DEBUG N ",n)
        if(c==10001):
            print("10001th prime is %d."%n)
            break
    else:
        pass
