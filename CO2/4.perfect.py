perfect=[]

for n in range(1000,10000):
    i=1
    while i*i<n:
        i+=1
    if i*i==n and all(d in '0149' for d in str(n)):
        perfect.append(n)

print(perfect)
