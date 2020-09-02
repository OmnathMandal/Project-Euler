n=int(input("type the 1000 digit number :"))
d=int(input("Type the number of digits you want to check :"))
greatest=0
list=[]
while n>0 :
    product=1
    s=0
    list=[]
    m=n
    for i in range (1,d+1):
        s=int(m%10)
        list.append(s)
        product*=s
        m=m//10
    if greatest<product:
        greatest=product
        list2=list
    n=n//10    

for j in range(d-1,-1,-1):
    if j==0:
        print("%d = %d"%(list2[0],greatest))
    else:
        print("%d*"%list2[j],end="")
