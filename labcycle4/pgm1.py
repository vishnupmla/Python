class Rectangle:
    def __init__(self,length,breadth) -> None:
        self.l=length
        self.b=breadth
    def area(self):
        rslt = self.l*self.b
        print("Area of rectangle = ",rslt)
        return rslt
    
    def perimeter(self):
        rslt = (self.l+ self.b)*2
        print("Perimeter of rectangle = ",rslt)
        return rslt

ob1 = Rectangle(5,3)
ob2 = Rectangle(12,8)
p= ob1.area()
q= ob1.perimeter()

ob2.area()

if(p > q):
    print("The area of object 1 is greater than object 2")
else:
    print("Area of object 2 is greater")