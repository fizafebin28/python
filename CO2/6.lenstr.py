string=input("Enter a string: ")
print("No of characters: ",len(string))
print()
for ch in set(string):
    print(ch,"=",string.count(ch))
