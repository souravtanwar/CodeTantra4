

a= list(map(int, input("Enter a multiple value: ").split()))
n =len(a)
for i in range(1,n):
    temp = a[i]
    j = i-1
    while j>=0 and a[j] >temp:
        a[j+1] = a[j]
        j =j-1
    a[j+1] =  temp
    print(a)

