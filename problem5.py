flag=True
def check(num):
    c=0
    for i in range(1,21):
        if num%i==0:
            c+=1
    if(c==10):
        return True
    else :
        return False


n=0
while(flag):
    n+=1
    if check(n):
        flag = False
        if not flag:
            print("%d is the smallest number that can be divided by each of the numbers from 1 to 20 without any remainder."%(n))
            break
        else:
            pass
