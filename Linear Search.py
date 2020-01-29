#LINEAR SEARCH
n = int(input("Enter number of elements in the list: "))
li = input("Enter "+str(n)+" elements separated by space: ").split()
s = input("Enter the number to search: ")
print(li)
flag = 0
pos = 0
def linearSearch(li,s):
    for i in range (0,len(li)):
        if li[i] == s:
            return i+1;
    return -1;

r = linearSearch(li,s)
if r ==-1:
    print("element is not found ")
else:
    print("Item if found at: ", r)