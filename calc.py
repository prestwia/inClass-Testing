class calc:    
    def add(self, a, b):
        if (type(a) is not int or type(b) is not int):
            return "only ints allowed"
        else:
            return a + b
    
    def subtract(self, a, b):
        if (type(a) is not int or type(b) is not int):
            return "only ints allowed"
        else:
            return a - b
    
    def multiply(self, a, b):
        if (type(a) is not int or type(b) is not int):
            return "only ints allowed"
        else:
            return a * b

    def divide(self, a, b):
        if (type(a) is not int or type(b) is not int):
            return "only ints allowed"
        else:
            if (b == 0):
                return "undefined"
            else:
                return a / b

    
    
    

