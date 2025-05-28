class p:
    def __init__(self,x=5, y=15):
        self.x=x
        self.y=y
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

x=p(50,100)
print(x)