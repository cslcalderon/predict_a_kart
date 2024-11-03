class Map:
    def __init__(self, name, obstacles, slipperiness, curvy):
        self.name = name
        self.obstacles = obstacles
        self.slipperiness = slipperiness
        self.curvy = curvy

    def get_name(self):
        return self.name
    
    def get_slipperiness(self):
        return self.slipperiness
    
    def get_curvy(self):
        return self.curvy