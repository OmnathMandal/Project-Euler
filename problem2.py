n = int(input("Type the value for N : "))
a=1
b=2
print("-----fibonacci series-----")
print(a)
print(b)
for i in range(2,n):
    k=a+b
    print(k)
    a=b
    b=k
