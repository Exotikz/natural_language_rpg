from World import *

class Race(World):
    
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_place(self):
        return self.place

    def set_place(self, place):
        self.place = place