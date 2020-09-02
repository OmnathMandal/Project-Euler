def sum(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=(i**2)
    return sum


def sumation(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    return sum**2


def difference(start,end):
    return sumation(start,end)-sum(start,end)


print("The difference is %d ."%difference(1,100))
