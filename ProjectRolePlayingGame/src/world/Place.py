from World import *

class Place(World):
    
    def __init__(self, name, biome):
        self.name = name
        self.biome = biome

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_biome(self):
        return self.biome

    def set_biome(self, biome):
        self.biome = biome