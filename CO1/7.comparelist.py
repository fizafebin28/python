x=list(map(int,input("Enter first list of numbers: ").split()))
y=list(map(int,input("Enter second list of numbers: ").split()))

print("a) Same Length: ",len(x)==len(y))
print("b) Same Sum: ",len(x)==len(y))
print("c) Same Value: ",set(x)&set(y))
