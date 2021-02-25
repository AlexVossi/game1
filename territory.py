class Territory: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color
        self.borders = []
        self.owner = None
        self.troops = 0

    def add_troops(self, number):
        self.troops = self.troops + number 

    def takeover(self, new_owner):
        self.owner = new_owner

    def remove_troops(self, number):
        self.troops = self.troops - number

    def add_borders(self, areas):
        for area in areas:
            self.borders.append(area)
        

    #def move_troops(self, )    