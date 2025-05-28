class car:
    __x=55
    def __f1(self):
        print("Private fuction")
    
    def f2(self):
        print("Public function")
        print(self.__x)

o=car()

o.f2()
o.__f1
print(o.__x)