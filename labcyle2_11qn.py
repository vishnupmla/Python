#Area of square

a= lambda s: s*s
print('The area of the square is: \n',a(int(input('Enter the side of the square- '))))

#Area of rectangle
b=lambda l,b: l*b

print('The area of the rectangle is: \n',b(int(input('Enter the length of the rectangle- ')),int(input('Enter the breadth- '))))

#Are of triangle
c= lambda b,h: 0.5*b*h
print('The area of the Triangle is: \n',c(int(input('Enter the base of the triangle - ')),int(input('Enter the height- '))))
