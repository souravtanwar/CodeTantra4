#QUICK SORT
a = [int(x) for x in input("Enter a multiple value: ").split()]

def partition(a,low,high):
    pivot =a[high]
    i= low-1
    for j in range(low,high):
        if a[j]<pivot:
            i = i+1
            a[i],a[j]= a[j],a[i]

    a[i+1],a[high] =a[high],a[i+1]
    return (i+1)

def quicksort(a,low,high):
    if low< high:
        pi = partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)

n = len(a)
quicksort(a,0,n-1)
print(a)