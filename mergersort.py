# MERGE SORT
def ms(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        ms(l)
        ms(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

def printlist(arr):
    print(arr)
if __name__ == '__main__':
    arr = [int(x) for x in input("Enter a multiple value: ").split()]
    print("Given array is:", end ="\n")
    printlist(arr)
    ms(arr)
    print("Sorted array is: ",end="\n")
    printlist(arr)