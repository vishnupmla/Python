class Rectangle:
    def __init__(self,len,wid) -> None:
        self.__len = len
        self.__wid = wid
    def rect_area(self):
        rslt = self.__len*self.__wid
        return(rslt)
    def __lt__(self, other):
        return self.rect_area() < other.rect_area()
    
ob1 = Rectangle(4,3)
ob2 = Rectangle(5,2)

if ob1 < ob2:
    print('The area of rectangle 2 is greater')
else:
    print('The area of rectangle 1 is greater')
        