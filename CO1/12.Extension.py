file=input("Enter the file name: ")
if "." in file:
    print("Extension: ",file.split(".")[-1])
else:
    print("Extension not found!!!")
