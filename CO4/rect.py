class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)

l1=int(input("Enter 1st rectangle length: "))
b1=int(input("Enter 1st rectangle breadth: "))
r1=Rectangle(l1,b1)
print("Rectangle 1\n\tArea:",r1.area(),"\n\tPerimeter:",r1.perimeter())

l2=int(input("\nEnter 2nd rectangle length: "))
b2=int(input("Enter 2nd rectangle breadth: "))
r2=Rectangle(l2,b2)
print("Rectangle 2\n\tArea:",r2.area(),"\n\tPerimeter:",r2.perimeter())

if r1.area()>r2.area():
    print("\nRectangle 1 is larger")

elif r1.area()<r2.area():
    print("\nRectangle 2 is larger")

else:
    print("\nBOTH ARE EQUAL")
