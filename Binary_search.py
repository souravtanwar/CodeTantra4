#BINARY SEARCH
a= list(map(int, input("Enter a multiple value: ").split()))
print(a)
n =len(a)
h= n
l = 0
key = int(input("Enter the key"))
"""flag =0
l = 0
while l<=h :
    mid = int((l+h)/2)
    if a[mid] == key:
        pos = mid +1
        flag =1
        break
    elif(key > a[mid]):
        l = mid+1
    elif key < a[mid]:
        h =mid -1
if flag == 1:
    print("The key element {} is found at {}".format(key, pos))
else:
    print("key is not in array")"""

def BS(a,l,h,key):
    mid = int((l + h) / 2)
    if a[mid] == key:
        return mid +1
    elif (key > a[mid]):
        return BS(a,mid+1,h,key)
    elif key < a[mid]:
        return BS(a,l,mid-1,key)
    else:
        return -1

r= BS(a,0 ,len(a)-1,key)

if r != -1:
    print("Element is present at index ",r)
else:
    print("Element is not in the array")

