# class computer: #Creating a class
#     def display(self): # creating a function
#         print("display this")
# hp=computer() # create a object
# hp.display()


# class computer:
#     def __init__(self):  #Buildin function name
#         print("display computer")
# hp=computer()   # creating a object


class computer:
    def __init__ (self):
        self.ram=""
        self.processor=""
        self.price=""
    def display(self):
        print("Ram = ",self.ram)
        print("Processer = ",self.processor)
        print("Price = ",self.price)
hp=computer()

hp.ram="10Gb"
hp.processor="i5"
hp.price="10,000"
hp.display()

