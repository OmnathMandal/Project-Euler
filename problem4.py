def ispalindrome(n):
    m=n
    s=0
    p=0
    while(n>0):
        s=int(n%10)
        p=int(s+(p*10))
        n=int(n/10)
    if p==m:
        return 1
    else:
        return 0

product=0
largest=0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        flag=False
        product=0
        product=i*j
        if (ispalindrome(product))==1:
            if product>largest:
                n1=i
                n2=j
                largest=product

print("%d x %d ="%(n1,n2),largest)
