a=int(input("Enter first value: "))
b=int(input("Enter second value: "))

while b:
    a,b=b,a%b

print("GCD= ",a)
