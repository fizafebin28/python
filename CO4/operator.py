class Rect:
    def __init__(self,l,w):
        self.__l=l
        self.__w=w

    def area(self):
        return self.__l*self.__w

    def __lt__(self,other):
        return self.area()< other.area()


l1=float(input("Length 1: "))
w1=float(input("Width 1: "))
r1=Rect(l1,w1)

l2=float(input("\nLength 2: "))
w2=float(input("Width 2: "))
r2=Rect(l2,w2)

print("\n",r1<r2)
