string=input("Enter a string: ")

if  not 'ing' in string:
    print(string[0:-1]+'ing')
elif 'ing' in string:
    print(string+'ly')
