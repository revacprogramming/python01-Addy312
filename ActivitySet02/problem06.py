

class Menu:
    def __init__(self):
      self.items=[]
    def add(self,item,quan):
      self.items.append((item,quan))


m = Menu()  #Menu is a class
m.add("idly", 10)
m.add("vada". 20)

m.show()
