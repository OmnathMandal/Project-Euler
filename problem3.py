def prime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
            break
    if(c==0):
        return 1
    else:
        return 0


def largest(n1):
    lpf=0
    for j in range(int(n1**0.5),1,-1):
        print("DEBUG",j)
        if(n1%j==0):
            if prime(j)==1:
                lpf=j
                break
    print("The largest prime factor of",n1,"is",lpf)


num=int(input("Type the number whose largest prime factor need to be found : "))
largest(num)
