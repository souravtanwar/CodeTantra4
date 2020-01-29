#binary to decimal number
n=int(input("Enter a binary number: "))
x =0

for i in range(0,n):
    a = n % 10
    x += a*pow(2,i)
    n = n//10
print(x)