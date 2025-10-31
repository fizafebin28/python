clr1=input("Enter colors of list 1 (seperated by comma): ").split(",")
clr2=input("Enter colors of list 2 (seperated by comma): ").split(",")
x=[c for c in clr1 if c not in clr2]

print("colors in list 1 and not in list 2: ",x)
