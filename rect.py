
class Rectangle:
    """This is rectange class used for determinig the area of rectangle"""
    c = 0
    def __init__(self,height,width):
        self.height = height
        self.width = width
        Rectangle.c += 1
    def show_(self):
        for key,value in self.__dict__.items():
            print(key,"=",value)
    def area(self):
        print("Area : ",self.height*self.width)
    def total():
        return Rectangle.c
    def __str__(self):
        return f"{self.height},{self.width}"
    def __del__(self):
        print("Deleting object....")
        sleep(2)
        del self
    
    
if __name__ == "__main__":
    from time import sleep
    r1 = Rectangle(10,30)
    r2 = Rectangle(100,30)
    print(r1)
    print(r2)
    r1
    r1.show_()
    r1.area()
    r2.show_()
    r2.area()
    
    del r1
    r1.show_()
