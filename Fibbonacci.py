#FIBBONACCI
def fibb(n):
    if n <0:
        return "INORRECT INPUT"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
n = int(input("Enter the number: "))
r = fibb(n)
print(r)