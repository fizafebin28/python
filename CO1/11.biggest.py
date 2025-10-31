x=int(input("Enter first digit: "))
y=int(input("Enter second digit: "))
z=int(input("Enter third digit: "))

if x>y and x>z:
    print(f"{x} is greater")
elif y>z:
    print(f"{y} is greater")
else:
    print(f"{z} is greater")


print("biggest is ",max(x,y,z))
