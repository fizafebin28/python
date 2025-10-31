d={3:'apple',4:'grape',1:'orange',2:'banana'}

print("Ascending: ",sorted(d.items()))
print("Descending: ",sorted(d.items(),reverse=True))

d=eval(input("\nEnter a dictionary: "))

print("Ascending: ",sorted(d.items()))
print("Descending: ",sorted(d.items(),reverse=True))
