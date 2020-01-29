
def reverse(s):
    s = "".join(reversed(s))
    return s
s= input("enter the number")
j = str(s)
print ("The reversed string(using reversed) is : ",end="")
print(reverse(j))
