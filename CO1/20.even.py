x=list(map(int,input("Enter a list of numbers: ").split()))

result=[n for n in x if n % 2!= 0 ]
print("Result= ",result)
