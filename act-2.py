class computer:
    def __init__(self):
        self.__mp=50000
    
    def sell(self):
        print("Price:", self.__mp)
    
    def setmp(self,p):
        self.__mp=p

o=computer()
o.sell()
o.__mp=70000
o.sell()
o.setmp(70000)
o.sell()