x=int(input("Enter current year: "))
n=int(input("Enter final year: "))

for i in range(x,n+1):
    if(i%4==0 and i%100!=0)or(i%400==0):
        print(i)
    
