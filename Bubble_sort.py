
#a= list(map(int, input("Enter a multiple value: ").split()))
a = [int(x) for x in input("Enter a multiple value: ").split()]
#print(b)
n = len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            temp =a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)