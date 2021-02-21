class Territory: 
    def __init__(self, name, color, borders): 
        self.name = name
        self.borders = borders 
        self.color = color
        self.owner = Null
        self.troops = 0

    def add_troops(self, number):
        self.troops = self.troops + number 

    def takeover(self, new_owner):
        self.owner = new_owner