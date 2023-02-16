#2 (length × breadth + breadth × height + length × height) area
# 4 (length + breadth + height) perimeter

def cubo_area(len,bre,h):
    rslt = (len*bre)+(bre*h)+(len*h)
    print("Area of Cuboid = ",rslt)

def cubo_perimeter(len,bre,h):
    rslt = len+bre+h
    print("Perimeter of cuboid = ",rslt)