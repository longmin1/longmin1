'''
编写一个Python程序，创建一个几何图形计算程序，
使用静态方法来计算矩形的面积和周长。
'''

class Rectangle():

    @staticmethod
    def area(length,width):
        result=length*width
        return (f"该矩形的面积是{result}")

    @staticmethod
    def perimeter(length,width):
        result=(length+width)*2
        return (f"该矩形的周长是{result}")

length,width=10,5
print(Rectangle.area(length,width))
print(Rectangle.perimeter(length, width))