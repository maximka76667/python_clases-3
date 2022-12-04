class Punto:
    def __init__(self, x, y, name="Punto"):
        self.__x = x
        self.__y = y
        self.__name = name
        
    def set_name(self, name):
        self.__name = name
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_name(self):
        return self.__name
    
    def desplazar_x(self, x):
        self.__x += x
        
    def desplazar_y(self, y):
        self.__y += y
        
    def show_info(self):
        print(self.__name + "(" + str(self.__x) + "," + str(self.__y) + ")", end="")
        
