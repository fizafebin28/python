n=int(input("Enter the no of terms: "))
a,b=0,1
print("\nFibonacci series: ")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
