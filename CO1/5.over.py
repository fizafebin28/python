num=input("Enter numbers: ").split()
lst=[]
for n in num:
    if int(n)>100:
        lst.append('over')
    else:
        lst.append(int(n))

print(lst)

