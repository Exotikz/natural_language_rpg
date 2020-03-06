

class World:
    
    def __init__(self, date, places, races):
        self.date = date
        self.places = places
        self.races = races

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_places(self):
        return self.places

    def set_places(self, places):
        self.places = places
    
    def get_races(self):
        return self.races

    def set_races(self, races):
        self.races = races

    def all_char_bio(self):
        # pseudo-language :
        # for all character that live in this world
        # |   list_of_bios.append(char.bio) 
        # return list of bios
        pass
        