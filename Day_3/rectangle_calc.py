import rectangle
#from rectangle import AREA
#from rectangle import PERIMETER
#from rectangle import *
#import rectangle as rectangle

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area_of_rectangle = rectangle.AREA(length,width)
    perimeter_of_rectangle = rectangle.PERIMETER(length,width)

    print(area_of_rectangle)
    print(perimeter_of_rectangle)

if __name__ == "__main__":
    main()

