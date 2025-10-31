text=input("Enter a line of text: ")
words=text.split()
for ch in set(words):
    print(ch,"-",words.count(ch))
    
